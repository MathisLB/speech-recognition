import torch
import sentencepiece as spm
sp = spm.SentencePieceProcessor()
sp.load("speechbrain/templates/speech_recognition/Tokenizer/save/1000_unigram.model")

# Encode as pieces
print(sp.encode_as_pieces('THE CITY OF MONTREAL'))

# Encode as ids
print(sp.encode_as_ids('THE CITY OF MONTREAL'))