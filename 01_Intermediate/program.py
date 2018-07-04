# import re
#
#
# text="what is the  price of dry chilli?"
#
# products=["rice","dry chilli","wheat","apple","banana"]
#
# # remove extra white spaces
# # text_formatted =  re.sub(' +',' ',text)
# words =  re.split('\s+', text)
# for t in words:
#     print t
#
# print reduce(lambda x,y: x + ' '+ y, words)


#implementation of __dict__ method
class Dog():
     def __init__(self,name):
         self.name = name
     # def __str__(self):
     #     return "My dog's name is %s"%(self.name)
V = Dog(name='sammy')
# print V.__str__()
#your output should give what you entered in your class
"My dog's name is sammy"

print V