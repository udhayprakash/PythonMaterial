#!/usr/bin/python
"""
Purpose: NLTK 
    Stemming vs Lemmatization
- While stemming can create words that do not actually 
  exist, Python lemmatization will only ever result in 
  words that do. lemmas are actual words.
"""
import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

ps = PorterStemmer()
lz = WordNetLemmatizer()

words = ['child', 'children', 'childhood', 'childs',
         'indetify']

for word in words:
    print(f"{word:12}: {ps.stem(word)}")
    print(f"{word:12}: {lz.lemmatize(word)}\n")
