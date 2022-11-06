import os
import re
import zipfile

import requests
import wget


def download_all_zips_files():
    """
    This function, perform get requests from the NVD site for all vulnerabilities data files which finish with ".json.zip"
    Finally the function writes all the files to NVD folder on the local disk
    :return:
    """
    r = requests.get("https://nvd.nist.gov/vuln/data-feeds#JSON_FEED")
    for filename in re.findall("nvdcve-1.1-[0-9]*\.json\.zip", r.text):
        r_file = requests.get(
            "https://nvd.nist.gov/feeds/json/cve/1.1/" + filename, stream=True
        )
        os.makedirs("nvd", exist_ok=True)
        with open("nvd/" + filename, "wb") as f:
            for chunk in r_file:
                f.write(chunk)


def download_file():
    url = "https://nvd.nist.gov/feeds/xml/cpe/dictionary/official-cpe-dictionary_v2.3.xml.zip"
    wget.download(url)
    # r_file = requests.get(source_url, stream=True)
    # with open(file_name, 'wb') as f:
    #     for chunk in r_file:
    #         f.write(chunk)


def unzip_file(file_name, directory_to_extract=None):
    with zipfile.ZipFile(file_name, "r") as zip_ref:
        zip_ref.extractall(directory_to_extract)
    os.remove(file_name)  # removing the .zip file


if __name__ == "__main__":
    download_file()
    download_all_zips_files()
