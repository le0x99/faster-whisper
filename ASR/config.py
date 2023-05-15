cfg = {'user'   : {
                    'audio_files_list'   : [],
                    'audio_files_dir'    : './some_audio_files',
                    'transcriptions_dir' : './some_transcriptions',
                    'language'  : None,
                   },

       'system' : {
                    'model_dir'   : './whisper-large-v2',
                    'device'      : 'cpu',
                    'device_idx'  : 0,
                    'num_workers' : 1,
                    'num_threads' : 1
                   },

       'model'  : {
                    'beam_size' : 5,
                    'best_of' : 5,
                    'patience' : 1,
                    'length_penalty' : 1,
                    'temperature' : [0., 0.2, 0.4, 0.6, 0.8, 1.0],
                    'compression_ratio_threshold' : 2.4,
                    'log_prob_threshold' : -1.,
                    'condition_on_previous_text' : True,
                    'initial_prompt' : None,
                    'prefix' : None,
                    'suppress_blank' : True,
                    'suppress_tokens' : [-1],
                    'without_timestamps' : False,
                    'max_initial_timestamp' : 1.,
                    'word_timestamps' : False,
                    'prepend_punctuations' : "\"'“¿([{-",
                    'append_punctuations'  :  "\"'.。,，!！?？:：”)]}、",
                    'vad_filter' : False,
                  }



       }

