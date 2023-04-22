#!/usr/bin/python3
"""
Purpose: To get the uncommon words
"""

word_set1 = {"San Francisco", "Los Angeles", "San Deigo"}
word_set2 = {"San Jose", "Los Angeles", "San Deigo", "Bakersfield"}

common_words = word_set1.intersection(word_set2)
print(f"{common_words =}")

uncommon_words = word_set1 ^ word_set2
print(f"{uncommon_words =}")
