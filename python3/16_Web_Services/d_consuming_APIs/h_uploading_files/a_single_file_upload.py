import random
import string

import requests


def create_dummy_file(name, max_length=1000):
    characters = string.ascii_letters + string.digits + string.punctuation
    with open(name, "w") as fh:
        sentence = "".join(
            [random.SystemRandom().choice(characters) for _ in range(max_length)]
        )
        fh.write(sentence)


def upload_file(file_name):
    url = "http://httpbin.org/post"

    fh = open(file_name, "rb")
    response = requests.post(url, files={"file": fh}, timeout=5)
    print(response.status_code)
    print(response.text)


if __name__ == "__main__":
    # create_dummy_file("myfile.txt")
    upload_file("myfile.txt")
