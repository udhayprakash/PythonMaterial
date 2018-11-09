# try:
# 	print string
# 	#a=1/0
# # except NameError:
# # 	print "string is not defined."
# # except ZeroDivisionError:
# # 	print "dividing by zero is not possible.s"
# except (NameError,ZeroDivisionError), error:
# 	print "Either NameError or ZeroDivisionError"
# 	print "The error is ", error
# else:
# 	print "Try clause worked succefully."
# finally:
# 	print "try may or may not get success"



# age = raw_input("please enter the age 1-150:")

# import exception

# class InvalidAgeRangeException(exception):
# 	def __init__(self,age):
# 		self.age = age

# 	def validate_age(age):
# 		if age < 0 or age > 150:
# 			raise InvalidAgeRangeException(age)

# try:
# 	age=int(age)
# 	validate_age(age)
# except ValueError as e:
# 	print e
# except InvalidAgeRangeException as e:
# 	print "Invalid age range, you entered : %s" % e.age


class MyError(Exception):
     def __init__(self, value):
        self.value = value
        print ""
     def str(self):
         return repr(self.value)


try:
	raise MyError(2*2)    #_=MyError(2*2)
except MyError as e:   #e= MyError()
	print 'My exception occurred, value:', e.value
	print "str value is", e.__str__()