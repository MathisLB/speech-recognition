import subprocess
import os

# Installer les bibliothèques nécessaires
subprocess.run(["pip", "install", "datasets"])

# Changer de répertoire
os.chdir("/content/speechbrain/templates/speech_recognition/LM")

# Exécuter le script d'entraînement
subprocess.run(["python", "train.py", "RNNLM.yaml"])  # Ajoutez --device='cpu' si nécessaire