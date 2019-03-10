import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")
    
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(5)
    counter = 0
    while counter < 36:
        brad.forward(100)
        brad.right(90)
        brad.forward(100)
        brad.right(90)
        brad.forward(100)
        brad.right(90)
        brad.forward(100)
        brad.right(100)
        counter += 1

    window.exitonclick()

if __name__ == "__main__":
    draw_square()
