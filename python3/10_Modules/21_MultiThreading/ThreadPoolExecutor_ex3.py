import io
import time
import requests
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

from PIL import Image
import numpy as np

IMAGE_FOLDER = Path(".").absolute() / "demo"


def download_image(img_url: str, save_loc: Path) -> np.ndarray:
    img_url = img_url.replace("\n", "")
    img_bytes = requests.get(img_url).content
    img_name = img_url.split("/")[-1].replace("\n", "")

    save_loc.mkdir(parents=True, exist_ok=True)

    with open(save_loc / img_name, "wb") as img_file:
        img_file.write(img_bytes)

    return np.array(Image.open(io.BytesIO(img_bytes)))


if __name__ == "__main__":
    start = time.perf_counter()

    with open(IMAGE_FOLDER / "demo_urls.txt", "r") as f:
        img_urls = [f.readline() for _ in range(10)]

    with ThreadPoolExecutor() as executor:
        for url in img_urls:
            executor.submit(download_image, url, IMAGE_FOLDER)

    finish = time.perf_counter()
    print(f"Finished in {round(finish-start, 2)} seconds")
