import re
#
#
text="what is the  price of dry chilli?"
#
products=["rice","dry chilli","wheat","apple","banana"]
#
# remove extra white spaces
text_formatted =  re.sub(' +',' ',text)
words =  re.split('\s+', text)
for t in words:
    print t
#
print reduce(lambda x,y: x + ' '+ y, words)
