import subprocess
import os

initial_dir = os.getcwd()
os.chdir("speechbrain/templates/speech_recognition/ASR")
subprocess.run(["python", "train.py", "train.yaml", "--number_of_epochs=1", "--batch_size=2", "--enable_add_reverb=False", "--enable_add_noise=False"])
os.chdir(initial_dir)