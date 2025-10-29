import os
import gdown


def download_from_drive(file_id, output_path):
    url = f"https://drive.google.com/uc?id={file_id}"
    print(f"📥 Downloading from Google Drive...\nURL: {url}")
    gdown.download(url, output_path, quiet=False)
    print(f"✅ Download complete! Saved as {output_path}")


if __name__ == "__main__":
    file_id = "1lcOZ5tcGYr9UMf9Eg0pYJpFkJxhXLwFJ"
    output_path = os.path.join("models", "similarity_matrices.pkl")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    download_from_drive(file_id, output_path)
