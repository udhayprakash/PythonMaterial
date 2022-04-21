#!/usr/bin/python
"""
Purpose: To access sharepoint content
"""
import urllib
import requests


def download_sharepoint_file(sharepoint_url, username, password, file_path):
    server = urllib.parse.ulrjoin(sharepoint_url, "/")
    auth = HTTPBasicAuth(username, password)
    headers = {"accept": "application/json;odata=verbose"}

    file_path = file_path.replace(" ", "%20")

    response = requests.get(
        file_path, auth=HttpNtlmAuth(domain + "\\" + username, password), stream=True
    )

    if response.status_code != 200:
        print(response.content)
        sys.exit(1)

    file_name = file_path.rsplit("/", maxsplit=1)[-1]

    with open(file_name, "wb+") as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
        f.close()
