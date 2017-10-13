#!/usr/bin/python
# http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/

def outer(func):
  def inner(*args,**kwargs):
    try:
      func(*args,**kwargs)
    except Exception as e:
      return e
    else:
      return func(*args,**kwargs)
  return inner


def div(a,b):
  return a/b
  
foo = outer(div)
print foo(4,2)
print foo(4,0)
  
 


'''
# Example 2

@outer
def div(a,b):
  return a/b

@outer 
def add(a,b):
  return a + b

print div(4,2)
div(4,0)
print add(2,3)
print add('a',3) 

# Example 1
def div(a,b):
  try:
    a/b
  except Exception as e:
    print e
  else:
    return a/b
    
def add(a,b):
  try:
    a + b
  except Exception as e:
    return e
  else:
    return a + b
  
    
print div(4,2)
div(4,0)
print add(2,3)
print add('a',3)
'''
