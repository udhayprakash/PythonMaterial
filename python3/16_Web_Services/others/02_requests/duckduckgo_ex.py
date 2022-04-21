#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Purpose: Usage of duckduckgo api
    https://duckduckgo.com/api

    pip install duckduckgo
"""

import sys

import duckduckgo

# print(dir(duckduckgo))

try:
    query_string = input("Enter the query:")
    response = duckduckgo.query(query_string)
except Exception as ex:
    print("request failed with error:", repr(ex))
    sys.exit(1)

# print(dir(response))
print("API version     :", response.api_version)
print("response.type   :", response.type)
print()

if response.type == "answer":  # DuckDuckGo
    print("answer url      :", response.abstract.url)
    print("answer source   :", response.abstract.source)
    print("No. of results  :", len(response.results))

    print()
    for each_result in response.results:
        print("each_result.url :", each_result.url)
        print("each_result.text:", each_result.text)
        # print('each_result.html:', each_result.html)
        # print('each_result.icon:', each_result.icon)
        # print(dir(each_result))
        print("-" * 30)
elif response.type == "disambiguation":  # Python
    print("No. of related  :", len(response.related))
    print()

    for each_result in response.related:
        print(each_result.url)
        print(each_result.text)
        if hasattr(each_result, "topic"):
            print("each_result.topic", each_result.topic)
        # print('each_result.html:', each_result.html)
        # print('each_result.icon:', each_result.icon)
        print("-" * 30)
    # print(dir(each_result))
elif response.type == "exclusive":  # 1+ 1
    print("response.answer.text:", response.answer.text)
    print("response.answer.type:", response.answer.type)
    print("No. of related      :", len(response.related))
    print(dir(response))
    print()

    for each_result in response.related:
        print(each_result.url)

        if hasattr(each_result, "topic"):
            print("each_result.topic", each_result.topic)
        # print('each_result.html:', each_result.html)
        # print('each_result.icon:', each_result.icon)
        print("-" * 30)
elif response.type == "nothing":  # 45654
    print(response.answer)
else:
    print("Unhandled response type:", response.type)
