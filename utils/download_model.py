import os
import gdown

def download_model_from_drive(file_id: str, output_path: str):
    if os.path.exists(output_path):
        return

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, output_path, quiet=False)