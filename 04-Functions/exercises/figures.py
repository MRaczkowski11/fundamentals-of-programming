# Function for drawing a square

import turtle                                                  # Importing the turtle module

pen = turtle.Turtle()                                          # Creating the turtle

def draw_square(length):                                       # Defining a function
    for i in range(4):                                         # Repeating four times
        pen.forward(length)                                    # Drawing one side
        pen.right(90)                                          # Turning right by 90 degrees