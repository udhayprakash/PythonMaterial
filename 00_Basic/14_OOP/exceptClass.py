# exceptClass.py

class TestClass(object):
    
    def __init__(self, name, number):

        self.name = name
        self.number = number
        
      

    def return_values(self):
        try:
            if (type(self.name) is int):
                return "The values are: ", type(self.name), type(self.number)
            else:
                raise notANumber(self.number)
        except notANumber as e:
            print("The value for number must be an int you passed: ", e.value)
            
        

class notANumber(Exception):
	def __init__(self, value):
		self.value = value

	def __str__(self):
		return repr(self.value)
