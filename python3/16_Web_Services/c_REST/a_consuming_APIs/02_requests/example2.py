import time

import requests
from tomorrow import threads


@threads(5)
def download(url):
    return requests.get(url, timeout=5)


if __name__ == "__main__":
    urls = [
        "http://google.com",
        "http://facebook.com",
        "http://youtube.com",
        "http://baidu.com",
        "http://yahoo.com",
    ]
    start = time.time()
    responses = [download(url) for url in urls]
    html = [response.text for response in responses]
    end = time.time()
    print("Time: %f seconds" % (end - start))

# solution for problem in python 3.7
# https://stackoverflow.com/questions/43948454/python-invalid-syntax-with-async-def
