import time
import math

def geom_average(x, y):
   if x<0 or y<0:
      raise Exception("Both x and y have to be positive")

   avg = math.sqrt(x*y)
   return avg

def timing_average(func):
   def wrapper(x, y):
      t0 = time.time()
      res = func(x, y)
      t1 = time.time()
      print("It took {} seconds to calculate the average".format(t1-t0))
      return res

   return wrapper

new = timing_average(geom_average)
new(2, 4)

# Syntactic Sugar for Decorators
@timing_average
def average(x, y):
   return (x+y)/2

avg = average(4, 6)
print('The average between 4 and 6 is {}'.format(avg))


#######################
def check_positive(func):
   def func_wrapper(x, y):
      if x<0 or y<0:
         raise Exception("Both x and y have to be positive for function {} to work".format(func.__name__))
      res = func(x,y)
      return res
   return func_wrapper


@check_positive
def average(x, y):
   return (x + y)/2

@check_positive
def geom_average(x, y):
   return math.sqrt(x*y)


average(2, 4)
try:
    average(-2, 4)
except Exception as ex:
    print ex

geom_average(4, 9)
try:
    geom_average(-4, 10)
except Exception as ex:
    print ex




@timing_average
@check_positive
def average(x, y):
   return (x + y)/2


print 'average(12, 12)=', average(12, 12)