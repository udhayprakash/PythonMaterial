#!usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 03 03:47:43 2016

@author: upethakamsetty
"""
__author__ = "Udhay Prakash Pethakamsetty"
__version__ = "1.0"

import functools

import urllib2


def with_retries(f):
    @functools.wraps(f)
    def g(*args):
        for i in range(5):
            try:
                return f(*args)
            except:
                print("Failed to download, retrying..")
        print("Giving up!")

    return g


@with_retries
def wget(url):
    return urllib2.urlopen(url)


# means wget = with_retries(wget)

wget("http://google.com/no-such-page")
