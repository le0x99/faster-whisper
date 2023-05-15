from config import cfg
import logging
from faster_whisper import WhisperModel
import os
import time
import json

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)

if __name__ == '__main__':
    logging.info(f'Loading model from {cfg["system"]["model_dir"]}.')
    model = WhisperModel(
                        model_size_or_path=cfg["system"]["model_dir"],
                        device=cfg["system"]["device"],
                        device_index=cfg["system"]["device_idx"],
                        compute_type='int8',
                        cpu_threads=cfg["system"]["num_threads"],
                        num_workers=cfg["system"]["num_workers"]
                        )
    logging.info('Model initialized.')
    source_dir = cfg["user"]["audio_files_dir"]
    if source_dir is not None:
        logging.info(f'Transcribing files in directory {source_dir}.')
        files_list = [source_dir + fname if source_dir.endswith('/') else source_dir + '/' + fname for fname in os.listdir(source_dir)]
        logging.info(f'Found a total of {len(files_list)} viable audio files.')
    else:
        files_list = cfg["user"]["files_list"]

    # lang = 'auto' if cfg["user"]["expected_language"] is None else cfg["user"]["expected_language"]
    n_files = len(files_list)
    target_dir = cfg["user"]["transcriptions_dir"]
    logging.info(f'Transcriptions will be saved to {target_dir}.')
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    logging.info(f'Starting transcribing {n_files} audio files.')
    for i, file_loc in enumerate(files_list):
        start = time.time()
        logging.info(f'Loading file from {file_loc}.')
        chunks, info = model.transcribe(audio=file_loc, **cfg["model"])
        logging.info(f'Transcribing audio file.')
        chunks = list(chunks)
        end = time.time()
        logging.info(f'Success - Transcription complete [{i+1}/{n_files}].')
        target_name = f'{target_dir}{file_loc.split("/")[-1].split(".")[0]}.json' if target_dir.endswith("/") else f'{target_dir}/{file_loc.split("/")[-1].split(".")[0]}.json'
        res = {field : getattr(info, field) for field in info._fields }
        res["chunks"] = [{field : getattr(chunk, field) for field in chunk._fields } for chunk in chunks]
        res["transcription_duration"] = end - start
        logging.info(f'Writing transcription file to {target_name}')
        with open(target_name, "w") as f:
            json.dump(res, f)
