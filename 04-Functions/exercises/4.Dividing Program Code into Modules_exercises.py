# 1. Program for testing the converters module======================================================================================================================================================================

import converters                                             # Importing the converters module

cm = 100
result = converters.cm_to_inches(cm)                          # Converting centimeters to inches
print(f'{cm} centimeters is {result} inches')

feet = 5
inches = 8
result = converters.feet_inches_to_cm(feet, inches)           # Converting feet and inches to centimeters
print(f'{feet} feet and {inches} inches is {result} centimeters')

# 2. Allows to enter and print employee data. Due to personal data protection,======================================================================================================================================================================
# you can determine whether information about the employee's salary will be printed

import keyboard1                                               # Importing your own keyboard module

# Reads employee's data from keyboard
first_name = keyboard1.input_string('Enter name: ')             # Reading first name
last_name = keyboard1.input_string('Enter surname: ')           # Reading last name
age = keyboard1.input_integer('Enter age: ')                    # Reading age
salary = keyboard1.input_real('Enter salary: ')                 # Reading salary
is_salary_hidden = keyboard1.input_boolean('Hide salary? (y/n) ')  # Checking if salary should be hidden

# 3. Prints employee's record======================================================================================================================================================================
print('DATA RECORD')
print('===========')
print('Name:', first_name, last_name)
print('Age:', age)

if not is_salary_hidden:                                       # Checking if salary is not hidden
    print('Salary:', salary)

# 4. Program for drawing a square using a separate module======================================================================================================================================================================

import turtle                                                  # Importing the turtle module
import figures                                                 # Importing the figures module

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Draw a square
figures.draw_square(100)                                       # Drawing a square with side length 100

# Hide the turtle and finish
figures.pen.hideturtle()
window.mainloop()

# 5. Draws each of the figures twice in different locations======================================================================================================================================================================

import turtle                                                  # Importing the turtle module
import figures2                                                 # Importing the figures module

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = figures2.pen
pen.speed(5)

# Draw figures
figures2.draw_square(100)                                       # Drawing the first square

pen.penup()
pen.goto(-200, 100)                                            # Moving to a different location
pen.pendown()
figures2.draw_square(100)                                       # Drawing the second square

pen.penup()
pen.goto(100, 100)
pen.pendown()
figures2.draw_triangle(100)                                     # Drawing the first triangle

pen.penup()
pen.goto(250, 100)
pen.pendown()
figures2.draw_triangle(100)                                     # Drawing the second triangle

pen.penup()
pen.goto(-200, -100)
pen.pendown()
figures2.draw_rectangle(120, 70)                                # Drawing the first rectangle

pen.penup()
pen.goto(50, -100)
pen.pendown()
figures2.draw_rectangle(120, 70)                                # Drawing the second rectangle

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()

