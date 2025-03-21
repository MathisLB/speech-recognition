if __name__ == "__main__":
    import subprocess
    import os
    import shutil

    initial_dir = os.getcwd()
    source_prepare_script_path = os.path.join(initial_dir, "speechbrain/templates/speech_recognition/mini_librispeech_prepare.py")

    destination_dir = os.path.join(initial_dir, "speechbrain/templates/speech_recognition/ASR")

    destination_prepare_script_path = os.path.join(destination_dir, "mini_librispeech_prepare.py")

    if not os.path.isfile(source_prepare_script_path):
        raise FileNotFoundError(f"Le script {source_prepare_script_path} n'a pas été trouvé.")

    shutil.copy(source_prepare_script_path, destination_prepare_script_path)

    subprocess.run([
        "python", source_prepare_script_path,
        "--data_folder=your_data_folder",
        "--save_folder=your_save_folder"
    ], check=True)

    os.chdir(destination_dir)
    subprocess.run([
        "python", "train.py", "train.yaml",
        "--number_of_epochs=1",
        "--batch_size=2",
        "--enable_add_reverb=False",
        "--enable_add_noise=False",
        "--device", "cuda",
        "--num_workers=0"
    ], check=True)
    os.chdir(initial_dir)
