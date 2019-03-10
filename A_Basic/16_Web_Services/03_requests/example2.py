import time

import requests
from tomorrow import threads


@threads(5)
def download(url):
    return requests.get(url)


if __name__ == "__main__":
    urls = [
        'http://google.com',
        'http://facebook.com',
        'http://youtube.com',
        'http://baidu.com',
        'http://yahoo.com',
    ]
    start = time.time()
    responses = [download(url) for url in urls]
    html = [response.text for response in responses]
    end = time.time()
    print "Time: %f seconds" % (end - start)
