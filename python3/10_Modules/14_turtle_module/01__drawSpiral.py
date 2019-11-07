import turtle

my_turtle = turtle.Turtle()
myWin = turtle.Screen()


def drawSpiral(_my_turtle, line_length):
    if line_length > 0:
        _my_turtle.forward(line_length)
        _my_turtle.right(90)
        drawSpiral(_my_turtle, line_length - 5)


drawSpiral(my_turtle, 100)
myWin.exitonclick()
