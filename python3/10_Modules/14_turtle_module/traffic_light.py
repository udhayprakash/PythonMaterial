#!/usr/bin/python
"""
Purpose: Traffic Light Simulation
"""
import turtle


def draw_signal_stand():
    """ Draw a nice housing to hold the traffic lights"""
    tess.pensize(3)
    tess.color('black', 'white')
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(157)
    tess.circle(40, 180)
    tess.forward(157)
    tess.left(90)
    tess.end_fill()


def circle(t, ht, colr):
    """Position turtle onto the place where the lights should be, and
    turn turtle into a big circle"""
    t.penup()
    t.forward(40)
    t.left(90)
    t.forward(ht)
    t.shape('circle')
    t.fillcolor(colr)


def advance_state_machine():
    global state_num  # The global keyword tells Python not to create a new local variable for state_num

    if state_num == 0:  # Transition from state 0 to state 1
        henry.color('darkgrey')
        alex.color('darkgrey')
        tess.color('green')
        wn.ontimer(advance_state_machine, 3000)  # set the timer to explode in 3000 milliseconds (3 seconds)
        state_num = 1
    elif state_num == 1:  # Transition from state 1 to state 2
        henry.color('darkgrey')
        alex.color('orange')
        wn.ontimer(advance_state_machine, 1000)
        state_num = 2
    elif state_num == 2:  # Transition from state 2 to state 3
        tess.color('darkgrey')
        wn.ontimer(advance_state_machine, 1000)
        state_num = 3
    else:  # Transition from state 3 to state 0
        henry.color('red')
        alex.color('darkgrey')
        wn.ontimer(advance_state_machine, 2000)
        state_num = 0


if __name__ == '__main__':
    # Create a playground for turtles
    wn = turtle.Screen()
    wn.bgcolor('skyblue')

    # Create turtles
    tess = turtle.Turtle()
    alex = turtle.Turtle()
    henry = turtle.Turtle()

    draw_signal_stand()

    circle(tess, 40, 'green')
    circle(alex, 100, 'orange')
    circle(henry, 160, 'red')

    # This variable holds the current state of the machine
    state_num = 0

    advance_state_machine()

    wn.listen()  # Listen for events

    wn.mainloop()  # Wait for user to close window
