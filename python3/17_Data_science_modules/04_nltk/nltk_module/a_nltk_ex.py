#!/usr/bin/python
"""
Purpose: NLTK
    Stemming words and sentences
"""
import nltk
from nltk.stem import PorterStemmer

ps = PorterStemmer()

# Stemming individual words
words = ["write", "writer", "writing", "writers"]
for word in words:
    print(f"{word:12}: {ps.stem(word)}")
print()

words = ["game", "gaming", "gamed", "games"]
for word in words:
    print(f"{word:12}: {ps.stem(word)}")
print()

words = ["child", "children", "childhood", "childs"]
for word in words:
    print(f"{word:12}: {ps.stem(word)}")
