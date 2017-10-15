#!/usr/bin/python
'''
Purpose: linkedList creation
'''
__author__ = 'Udhay Prakash'

class LinkedList:
    def __init__(self, initData):
        self.data = initData
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next()

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext


myLL = LinkedList(23)
print myLL.getData()
