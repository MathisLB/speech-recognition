from speechbrain.inference.ASR import EncoderDecoderASR

asr_model = EncoderDecoderASR.from_hparams(source="model/", hparams_file='your_file.yaml', savedir="model/")
audio_file = 'your_file.wav'
asr_model.transcribe_file(audio_file)