from speechbrain.inference.ASR import EncoderDecoderASR

asr_model = EncoderDecoderASR.from_hparams(source="results/CRDNN_BPE_960h_LM/2602/save", hparams_file='results/CRDNN_BPE_960h_LM/2602/hyperparams.yaml', savedir="modele_perso/")
audio_file = 'test.wav'
asr_model.transcribe_file(audio_file)