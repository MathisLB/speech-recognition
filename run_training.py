import subprocess
import os

# Changer de répertoire
os.chdir("/content/speechbrain/templates/speech_recognition/LM")

# Exécuter le script d'entraînement avec CUDA
subprocess.run(["python", "train.py", "RNNLM.yaml", "--device='cuda'"])