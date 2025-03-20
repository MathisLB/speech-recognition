import subprocess
import os

initial_dir = os.getcwd()
os.chdir("speechbrain/templates/speech_recognition/LM")
subprocess.run(["python", "train.py", "RNNLM.yaml", "--device=cuda"])
os.chdir(initial_dir)