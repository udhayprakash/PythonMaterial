#!/bin/python3

import json
import urllib.request


def getUsernames(threshold):
    records = []
    pageNumber = 1
    while True:
        url = f"https://jsonmock.hackerrank.com/api/article_users?page={pageNumber}"
        response = urllib.request.urlopen(url).read()
        content = json.loads(response)
        records.extend(
            [
                rec["username"]
                for rec in content["data"]
                if float(rec["submission_count"]) >= threshold
            ]
        )

        if content["page"] == content["total_pages"]:
            break
        pageNumber += 1
    return records


if __name__ == "__main__":
    result = getUsernames(2)
    print(result)
