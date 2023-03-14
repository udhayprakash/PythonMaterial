#!/usr/bin/python3
"""
Purpose: To read large file
"""
from functools import partial


def read_from_file(file_name):
    """Method 1 - reading one line per iteration"""
    with open(file_name, "r") as fp:
        yield fp.readline()


def read_from_file2(file_name, block_size=1024 * 8):
    """Method 2 - reading block size per iteration"""
    with open(file_name, "r") as fp:
        while True:
            chunk = fp.read(block_size)
            if not chunk:
                break
            yield chunk


def read_from_file3(file_name, block_size=1024 * 8):
    """Method 3 - reading block size per iteration (clean code)"""
    with open(file_name, "r") as fp:
        for chunk in iter(partial(fp.read, block_size), ""):
            yield chunk
