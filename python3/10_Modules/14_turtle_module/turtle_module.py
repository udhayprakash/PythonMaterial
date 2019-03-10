import turtle as t

#print "List of attributes in turtle module are\n"
#for i, j in enumerate(dir(t)):
#    print i, j

# print "help(t)", help(t)
#print "help(t.width)", help(t.width)

t.forward(100)  # same as fd(100)

t.shape("turtle")

#help(t.shape())

t.reset()# to reset the graphics window

for i in range(100):
	if i %2 == 0:
		t.forward(10)
		t.left(30)
	else:
		t.forward(10)
		t.right(30)

