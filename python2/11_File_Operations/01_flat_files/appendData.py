#!/usr/bin/python

'''
Purpose: To append data to existing test.txt
'''

g = open('test.txt', 'ab')  # opening in append mode

g.write('\n\n\tToday!, we are learning python file handling features')
g.close()
