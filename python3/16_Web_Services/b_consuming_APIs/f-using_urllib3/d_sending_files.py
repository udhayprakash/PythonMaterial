#!/usr/bin/python3
"""
Purpose:
"""
import json
import shutil

import urllib3

# Pool Manager
http = urllib3.PoolManager()


# Download data
def download_data_from_url(url, filepath, chunk_size=1024):
    r = http.request("GET", url, preload_content=False)

    with open(filepath, "wb") as out:
        while True:
            data = r.read(chunk_size)
            if not data:
                break
            out.write(data)

    r.release_conn()  # If given, poolmanager will reuse this connection


def download_data_from_url2(url, filepath, chunk_size=1024):
    with open(filepath, "wb") as out:
        r = http.request("GET", url, preload_content=False)
        shutil.copyfileobj(r, out)

    r.release_conn()


def uploading_data_to_url():
    with open("file_name.txt") as f:
        file_data = f.read()

    # Sending the request.
    resp = http.request(
        "POST",
        "https://reqbin.com/post-online",
        fields={
            "file": ("file_name.txt", file_data),
        },
    )

    print(json.loads(resp.data.decode("utf-8"))["files"])
