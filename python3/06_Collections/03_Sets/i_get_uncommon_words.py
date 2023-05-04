#!/usr/bin/python3
"""
Purpose: To get the uncommon words
    |   set union
    &   set intersection
    ^   set symmetric_difference
    <=  isubset
    >=  issuperset
"""

word_set1 = {"San Francisco", "Los Angeles", "San Deigo"}
word_set2 = {"San Jose", "Los Angeles", "San Deigo", "Bakersfield"}

all_words = word_set1 | word_set2
print(f"{all_words = }")

all_words = word_set1.union(word_set2)
print(f"{all_words = }")

common_words = word_set1 & word_set2
print(f"{common_words =}")

common_words = word_set1.intersection(word_set2)
print(f"{common_words =}")

uncommon_words = word_set1 ^ word_set2
print(f"{uncommon_words =}")

uncommon_words = word_set1.symmetric_difference(word_set2)
print(f"{uncommon_words =}")
print()

A = {1, 2}
B = {1, 2, 3, 4}
print(A <= B)  # Output: True
print(B >= A)  # Output: True
