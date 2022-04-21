#!/usr/bin/python
"""
Purpose: NLTK
    Stemming words and sentences
"""
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Stemming entire sentence
nltk.download("punkt")
ps = PorterStemmer()

sentence = "The quick brown fox jumps over the lazy dog"
sentence = """I am enjoying writing this tutorial;
I love to write and I have written 266 words so far.
I wrote more than you did; I am a writer."""

words = word_tokenize(sentence)
for word in words:
    print(f"{word:12}: {ps.stem(word)}")
