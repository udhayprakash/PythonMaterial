#!/usr/bin/python 

'''
	Purpose: module importing demonstration
	
	To create documenation for this script, use 
		python -m pydoc -w newScript
'''
vowels = 'aeiou'

luckyNumber = 1321

def firstFunction():
	'''
	This is firstFunction
	:return: None
	'''
	print("This is first function")
	

def addition(a,b):
	'''
		performs addition operation
		ex: addition(12, 34)
		returns: a+b 
	'''
	return a+b
	
def subtraction(a,b):
	'''
		performs subtraction operation
	'''
	return a-b
	
def multiplication(a,b):
	'''
		performs multiplication operation
	'''
	return a*b
	
	
print('__file__', __file__)
print('__name__', __name__)
if __name__ == '__main__':
	print('This script is executed directly')
else:
    print('This script is indirectly called ')