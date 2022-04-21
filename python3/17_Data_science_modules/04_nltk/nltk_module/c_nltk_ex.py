#!/usr/bin/python
"""
Purpose: NLTK
  Lemmatization
   - lets us group together inflected forms of a word.
   - It links words with similar meanings to one word
     and maps various words onto one root.
"""
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Lemmatization
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()

words = ['dog', 'dogs', 'geese', 'cacti', 'erasers', 'writers',
         'children', 'childhood', 'feet']
for word in words:
    print(f'{word:12}: {lemmatizer.lemmatize(word)}')
