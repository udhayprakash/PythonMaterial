#!/usr/bin/python

# Stack Abstract Data Type (ADT) Implementation
'''
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


s = Stack()  # Object Instantiation

print "s.is_empty() ", s.is_empty()

s.push(1234)
s.push('Python')
print "s = ", s
print "s.peek() ", s.peek()
s.push(True)
print "s.size()", s.size()
print "s.is_empty() ", s.is_empty()
s.push(23.45)
print "s.pop() ", s.pop()
print "s.pop() ", s.pop()
print "s.size() ", s.size()
'''

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items[0]

    def size(self):
        return  len(self.items)

s = Stack()

s.push('Hello world!')
s.push(True)
print "s.size()", s.size()
print 's.pop() ', s.pop()
print "s.size()", s.size()

#######################################################
# linkedList creation
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


###########
# RECURSIONS
###########
'''
Three Laws of Recursion:
------------------------
1. A recursive algorithm must have a base case.
2. A recursive algorithm must change its state and move toward the base case.
3. A recursive algorithm must call itself, recursively.
'''
# rec1.py
# calculating sum of a list of numbers

def sumOfList(numList):              # conventional implementation
    total = 0
    for i in numList:
        total+=i
    return total

print sumOfList([12, 23, 34, 546, 1])

def sumOfListRec(numList):           # implementation using recursions
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0]+sumOfListRec(numList[1:])

print sumOfListRec([12, 23, 34, 546, 1])




def toString(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toString(n/base, base) + convertString[n%base]

print toString(1453, 16)
print toString(1453, 8)

###################################################
'''
import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle, lineLen-5)

drawSpiral(myTurtle, 100)
myWin.exitonclick()
'''
#################################################
import turtle
def draw_triangle(points, color, my_turtle):
    my_turtle.fillcolor(color)
    my_turtle.up()
    my_turtle.goto(points[0][0],points[0][1])
    my_turtle.down()
    my_turtle.begin_fill()
    my_turtle.goto(points[1][0], points[1][1])
    my_turtle.goto(points[2][0], points[2][1])
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.end_fill()

def get_mid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points, degree, my_turtle):
    color_map = ['blue', 'red', 'green', 'white', 'yellow',
    'violet', 'orange']
    draw_triangle(points, color_map[degree], my_turtle)
    if degree > 0:
        sierpinski([points[0],
            get_mid(points[0], points[1]),
            get_mid(points[0], points[2])],
            degree-1, my_turtle)
        sierpinski([points[1],
            get_mid(points[0], points[1]),
            get_mid(points[1], points[2])],
            degree-1, my_turtle)
        sierpinski([points[2],
            get_mid(points[2], points[1]),
            get_mid(points[0], points[2])],
            degree-1, my_turtle)

def main():
    my_turtle = turtle.Turtle()
    my_win = turtle.Screen()
    my_points = [[-100, -50], [0, 100], [100, -50]]
    sierpinski(my_points, 3, my_turtle)
    my_win.exitonclick()

'''
exercises on recursions:
--------------------------
1. Write a recursive function to compute the factorial of a number
2. Write a recursive function to reverse a list
3. Write a recursive function to compute the fibonacci series


'''