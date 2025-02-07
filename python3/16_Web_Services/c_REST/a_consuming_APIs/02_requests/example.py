import time
from security import safe_requests


def download(url):
    return safe_requests.get(url, timeout=60)


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
    print(responses[0])
    # pdb.set_trace()
    html = [response.text for response in responses]
    end = time.time()
    print("Time: %f seconds" % (end - start))
