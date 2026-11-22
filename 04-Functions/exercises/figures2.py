# Functions for drawing geometric figures

import turtle                                                  # Importing the turtle module

pen = turtle.Turtle()                                          # Creating the turtle

def draw_square(length):                                       # Function for drawing a square
    for i in range(4):
        pen.forward(length)
        pen.right(90)

def draw_triangle(length):                                     # Function for drawing a triangle
    for i in range(3):
        pen.forward(length)
        pen.right(120)

def draw_rectangle(length_a, length_b):                        # Function for drawing a rectangle
    for i in range(2):
        pen.forward(length_a)
        pen.right(90)
        pen.forward(length_b)
        pen.right(90)
