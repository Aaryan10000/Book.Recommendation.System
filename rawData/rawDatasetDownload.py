# Create venv -- python -m venv BRSenv
# Activate venv -- source BRSenv/bin/activate
# Deactivate venv -- deactivate

from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()
api.dataset_download_files(
    "mexwell/best-books-ever", path=".", unzip=True)
