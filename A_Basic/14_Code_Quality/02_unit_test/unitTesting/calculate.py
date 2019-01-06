#!/usr/bin/python

__author__ = ''


class Calculate(object):
    def add(self, x,y):
        return x+y

if __name__ == '__main__':
    calc = Calculate()
    result = calc.add(2,2)
    print result