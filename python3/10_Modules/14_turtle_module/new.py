#!/usr/bin/python
"""
Purpose: Traffic Light Simulator
"""
import turtle

# constants
BG_COLOR = "#0080ff"  # sky-blue


class TrafficLightSimulator:
    def __init__(self):
        """
        Initial setup of the turtles
        """
        turtle.setup(400, 500)  # Determine the window size
        self.wn = turtle.Screen()  # Creates a playground for turtles
        self.wn.title("Traffic Light Simulator")  # Set the window title
        self.wn.bgcolor(BG_COLOR)  # Set the window background color
        self.green_signal = (
            turtle.Turtle()
        )  # Create a turtle, assign to self.green_signal
        self.orange_signal = turtle.Turtle()  # Create self.orange_signal
        self.red_signal = turtle.Turtle()  # Create self.red_signal

        self.draw_housing()

        self.__circle(self.green_signal, 50, "green")
        self.__circle(self.orange_signal, 120, "orange")
        self.__circle(self.red_signal, 190, "red")

        # This variable holds the current state of the machine
        self.state_num = 0
        self.advance_state_machine()
        self.wn.listen()  # Listen for events
        self.wn.mainloop()  # Wait for user to close window

    def draw_housing(self):
        """
        Draw a nice housing to hold the traffic lights
        :return:
        """
        self.green_signal.pensize(3)  # Change self.green_signal' pen width
        self.green_signal.color("black", "white")  # Set self.green_signal' color
        # self.green_signal.sety(-90)  # Tell self.green_signal to start filling the color
        self.green_signal.begin_fill()  # Tell self.green_signal to start filling the color
        self.green_signal.forward(
            80
        )  # Tell self.green_signal to move forward by 80 units
        self.green_signal.left(90)  # Tell self.green_signal to turn left by 90 degrees
        self.green_signal.forward(200)
        self.green_signal.circle(
            40, 180
        )  # Tell self.green_signal to draw a semi-circle
        self.green_signal.forward(200)
        self.green_signal.left(90)
        self.green_signal.end_fill()  # Tell self.green_signal to stop filling the color

    def __circle(self, t, ht, colr):
        """
        Position turtle onto the place where the lights should be, and
        turn turtle into a big circle.
        :param t: turtle object
        :param ht: height
        :param colr: fill color
        :return: None
        """
        t.penup()  # This allows us to move a turtle without drawing a line
        t.forward(40)
        t.left(90)
        t.forward(ht)
        t.shape("circle")  # Set tutle's shape to circle
        t.shapesize(3)  # Set size of circle
        t.fillcolor(colr)  # Fill color in circle

    def advance_state_machine(self):
        """
        A state machine for traffic light
        :return: None
        """

        if self.state_num == 0:  # Transition from state 0 to state 1
            self.red_signal.color("darkgrey")
            self.orange_signal.color("darkgrey")
            self.green_signal.color("green")
            self.wn.ontimer(
                self.advance_state_machine, 3000
            )  # set the timer to explode in 3 sec
            self.state_num = 1
        elif self.state_num == 1:  # Transition from state 1 to state 2
            self.red_signal.color("darkgrey")
            self.orange_signal.color("orange")
            self.wn.ontimer(self.advance_state_machine, 1000)
            self.state_num = 2
        elif self.state_num == 2:  # Transition from state 2 to state 3
            self.green_signal.color("darkgrey")
            self.wn.ontimer(self.advance_state_machine, 1000)
            self.state_num = 3
        else:  # Transition from state 3 to state 0
            self.red_signal.color("red")
            self.orange_signal.color("darkgrey")
            self.wn.ontimer(self.advance_state_machine, 2000)
            self.state_num = 0


# Program execution starts here
if __name__ == "__main__":
    TrafficLightSimulator()
