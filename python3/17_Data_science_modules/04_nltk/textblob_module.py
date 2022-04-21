#!/usr/bin/python
"""
To download the necessary data, simply run

    python -m textblob.download_corpora

or use the NLTK downloader to download the missing data: http://nltk.org/data.html
"""

from textblob import TextBlob

blob = TextBlob(
    """'I really enjoy programming in Python. It is a very approachable
language with a plethora of valuable, high quality, libraries in
both the standard library and as third party package from the
community"""
)

print(f"blob.sentiment: {blob.sentiment}")

for sentence in blob.sentences:
    print(sentence)
    print(sentence.sentiment)
    print()
