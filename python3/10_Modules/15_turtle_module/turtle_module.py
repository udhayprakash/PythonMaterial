import turtle as t

# print "List of attributes in turtle module are\n"
# for i, j in enumerate(dir(t)):
#    print i, j

# print "help(t)", help(t)
# print "help(t.width)", help(t.width)

t.forward(100)  # same as fd(100)

t.shape("turtle")

# help(t.shape())

t.reset()  # to reset the graphics window

for i in range(4):
    t.forward(100)
    t.left(90)

for i in range(0, 100, 10):
    t.square(i)
    t.left(90)
