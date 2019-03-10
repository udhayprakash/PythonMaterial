#!/usr/bin/python
"""
Purpose: linkedList creation

node1 -> node2  -> node3 , ...

each node:
    |data|address of next node
"""
__author__ = 'Udhay Prakash'


class LinkedList:
    def __init__(self, initData):
        self.data = initData
        self.nextDataLocation = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.nextDataLocation

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.nextDataLocation = newNext


myLL = LinkedList(23)
print 'myLL data = ', myLL.getData()
print 'myLL Next data location=', myLL.getNext()


myLL1 = LinkedList(999)
print 'myLL1 data = ', myLL1.getData()
print 'myLL1 Next data location=', myLL1.getNext()

myLL1.setNext(id(myLL))
print 'myLL1 Next data location=', myLL1.getNext()
