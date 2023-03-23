# File: jitterplot.py -- draw a jitter diagram (after XLispStat)
# Fredrik Lundh

import math
import random
from tkinter import *

GREY = "grey"
GREEN = "green"
WHITE = "white"
BLACK = "black"

#
# Draw jitterplot (should turn this into a compound widget instead)


def jitterplot(canvas, bbox, data):
    "Draw a jitter plot"

    # get min/max and average
    lo, hi = min(data), max(data)
    avg = sum(data) / float(len(data))
    var = sum(map(lambda a, m=avg: (a - m) * (a - m), data))
    sd = math.sqrt(var / float(len(data) - 1))

    # calculate scale
    ystep = (bbox[1] - bbox[3]) / (hi - lo)
    ybase = bbox[3]

    x = (bbox[2] + bbox[0]) / 2

    y0 = lo * ystep + ybase
    y1 = hi * ystep + ybase
    sd = sd * ystep

    # draw "cloud"
    y = (y0 + y1) / 2
    canvas.create_oval(x - sd, y0, x + sd, y1, fill=GREY, outline="")
    canvas.create_oval(x - sd, y - sd, x + sd, y + sd, fill=WHITE, outline="")

    # draw min/max and average bars
    y = avg * ystep + ybase
    w = 10
    canvas.create_line(x - w, y, x + w, y, fill=BLACK, width=3)
    canvas.create_line(x, y0, x, y1, fill=BLACK, width=3)
    canvas.create_line(x - w, y0, x + w, y0, fill=BLACK, width=3)
    canvas.create_line(x - w, y1, x + w, y1, fill=BLACK, width=3)

    # draw markers
    for y in map(lambda y, ys=ystep, yb=ybase: y * ys + yb, data):
        j = x + (y1 - y0) * 0.1 * (random.random() - 0.5)
        canvas.create_oval(j - 2, y - 2, j + 2, y + 2, fill=WHITE)


################################################################
# create some random data

data = [random.random() for a in range(200)]

# create a drawing canvas

root = Tk()

Label(text="Jitter Plot Example").pack()
canv = Canvas(root, height=500, width=500, bg=WHITE)
canv.pack()

# a few commands

##def printcanvas():
##    os.popen("lpr", "w").write(canv.postscript())

Button(text="Dismiss", command=root.quit).pack(side=LEFT)
##Button(text="Print", command=printcanvas).pack(side=LEFT)

# draw the diagram

bbox = 20, 20, 480, 480

jitterplot(canv, bbox, data)

root.mainloop()
