#!/usr/bin/python
"""
Purpose: Merge Sort 

MergeSort(List):
    if List consists of a single element:
        return List
    FirstHalf first half of List
    SecondHalf second half of List
    SortedFirstHalf MergeSort(FirstHalf)
    SortedSecondHalf MergeSort(SecondHalf)
    SortedList Merge(SortedFirstHalf;SortedSecondHalf)
    return SortedList

"""


def merge_sort(given_list):
    if len(given_list) == 1:
        return given_list
    first_half = given_list[:len(given_list) // 2]
    second_half = given_list[len(given_list) // 2:]

    sorted_first_half = merge_sort(first_half)
    sorted_second_half = merge_sort(second_half)

    sorted_list = merge(sorted_first_half, sorted_second_half)
    return sorted_list
