#!/usr/bin/env python

import requests


def download(url):
    """Download the given url and saves it to the current directory.

    :arg url: URL of the file to be downloaded.
    """
    req = requests.get(url)
    # First let us check non existing files.
    if req.status_code == 404:
        print("No such file found at %s" % url)
        return
    filename = url.split("/")[-1]
    with open(f"{filename}.html", "a+b") as fobj:
        fobj.write(req.content)
    print("Download over.")


if __name__ == "__main__":
    url = input("Enter a URL:")
    download(url)
