#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Purpose: Implementation of Single Linked List

In a linked list, each node will store a value and address of next node
"""
__author__ = "Udhay Prakash Pethakamsetty"


###########################
# UNDER DEVELOPMENT
#############################

class Node(object):
    def __init__(self, value):
        self.value = value
        self.address = None


linked_list = []
while True:
    try:
        number = int(raw_input('Enter an integer:'))
        linked_list.append(Node(number))
    except Exception as ex:
        print ex
