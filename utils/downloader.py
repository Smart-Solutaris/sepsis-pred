
import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_files():
    """Downloads all files from a given URL to a target directory."""
    target_dir = "dataset"
    for x in range(100001, 100101):
        filename = f"training_setB/p{str(x).zfill(6)}.psv"
        url = f"https://physionet.org/files/challenge-2019/1.0.0/training/{filename}?download"
        #href="/files/challenge-2019/1.0.0/training/training_setA/p000001.psv?download"
        filepath = os.path.join(target_dir, filename)  
        if os.path.exists(filepath): #
            continue
        else:
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
        try:
            print(f"Downloading: {url}") # Informative message

            file_response = requests.get(url=url, stream=True)  # Stream for large files
            file_response.raise_for_status()

            with open(filepath, "wb") as f:
                for chunk in file_response.iter_content(chunk_size=8192):  # Write in chunks
                    f.write(chunk)

            print(f"Downloaded: {filename}")

        except requests.exceptions.RequestException as e:
            print(f"Error downloading {url}: {e}")



if __name__ == "__main__":
    base_url = "https://physionet.org/files/challenge-2019/1.0.0/training_setA/"
    download_directory = "dataset/1/training_setA" 

    download_files()