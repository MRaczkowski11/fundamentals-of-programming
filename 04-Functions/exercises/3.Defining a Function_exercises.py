# 1. Calculates the area of a triangle based on the lengths of its sides======================================================================================================================================================================

import math                                                   # Importing the math module

def triangle_area(a, b, c):                                   # Defining a function with three parameters
    p = (a + b + c) / 2                                       # Calculating the semi-perimeter
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))         # Applying Heron's formula
    return area                                                # Returning the calculated area

side_a = float(input('Enter side a: '))                       # Reading the first side
side_b = float(input('Enter side b: '))                       # Reading the second side
side_c = float(input('Enter side c: '))                       # Reading the third side

result = triangle_area(side_a, side_b, side_c)               # Calculating the triangle area
print(f'The area of a triangle with sides {side_a}, {side_b}, {side_c} is {result}')

print('The area of a triangle with sides 3, 4, 5 is', triangle_area(3, 4, 5))
print('The area of a triangle with sides 5, 12, 13 is', triangle_area(5, 12, 13))
print('The area of a triangle with sides 7, 24, 25 is', triangle_area(7, 24, 25))

# 2. Calculates the sum of the digits in a number======================================================================================================================================================================

def sum_digits(number):                                       # Defining a function
    number = abs(number)                                      # Converting the number to its absolute value
    number_string = str(number)                               # Converting the number to a string
    total = 0                                                 # Initializing the sum

    for digit in number_string:                               # Going through each digit
        total = total + int(digit)                            # Adding the digit to the sum

    return total                                              # Returning the sum

any_number = int(input('Enter integer number: '))             # Reading an integer from the keyboard
result = sum_digits(any_number)                               # Calling the function

print(f'The sum of the digits in the number {any_number} is {result}')

# 3. Calculates the final grade for a test based on the number of points obtained======================================================================================================================================================================

def pts_to_grade(points):                                     # Defining a function
    grade = ''                                                # Initializing the grade

    if points >= 18:                                          # Checking if points are at least 18
        grade = 'Excellent'
    elif points >= 14:                                        # Checking if points are at least 14
        grade = 'Good'
    elif points >= 10:                                        # Checking if points are at least 10
        grade = 'Satisfactory'
    else:                                                     # If points are less than 10
        grade = 'Fail'

    return grade                                              # Returning the grade

test_result = 15                                              # Number of points obtained
final_grade = pts_to_grade(test_result)                       # Calculating the final grade

print(f'You scored {test_result} points on the test. Your final grade is {final_grade}')

# 4. Function that returns the full name of a day of the week based on its number======================================================================================================================================================================

def day_name(day_number):                                     # Defining a function
    result = ''                                               # Initializing the result

    if day_number == 1:
        result = 'Monday'
    elif day_number == 2:
        result = 'Tuesday'
    elif day_number == 3:
        result = 'Wednesday'
    elif day_number == 4:
        result = 'Thursday'
    elif day_number == 5:
        result = 'Friday'
    elif day_number == 6:
        result = 'Saturday'
    elif day_number == 7:
        result = 'Sunday'
    else:
        result = 'Invalid day number'

    return result                                             # Returning the day name

# Function usage
print('The name of day 5 in the week is', day_name(5))
print('The name of day 3 in the week is', day_name(3))
print('The name of day 7 in the week is', day_name(7))

# 5. Converts a name into ICAO phonetic alphabet words======================================================================================================================================================================

def icao(letter):                                              # Function that converts a letter to an ICAO word
    letter = letter.capitalize()                              # Capitalizing the letter

    if letter == 'A':
        icao_name = 'Alfa'
    elif letter == 'B':
        icao_name = 'Bravo'
    elif letter == 'C':
        icao_name = 'Charlie'
    elif letter == 'D':
        icao_name = 'Delta'
    elif letter == 'E':
        icao_name = 'Echo'
    elif letter == 'F':
        icao_name = 'Foxtrot'
    elif letter == 'G':
        icao_name = 'Golf'
    elif letter == 'H':
        icao_name = 'Hotel'
    elif letter == 'I':
        icao_name = 'India'
    elif letter == 'J':
        icao_name = 'Juliett'
    elif letter == 'K':
        icao_name = 'Kilo'
    elif letter == 'L':
        icao_name = 'Lima'
    elif letter == 'M':
        icao_name = 'Mike'
    elif letter == 'N':
        icao_name = 'November'
    elif letter == 'O':
        icao_name = 'Oscar'
    elif letter == 'P':
        icao_name = 'Papa'
    elif letter == 'Q':
        icao_name = 'Quebec'
    elif letter == 'R':
        icao_name = 'Romeo'
    elif letter == 'S':
        icao_name = 'Sierra'
    elif letter == 'T':
        icao_name = 'Tango'
    elif letter == 'U':
        icao_name = 'Uniform'
    elif letter == 'V':
        icao_name = 'Victor'
    elif letter == 'W':
        icao_name = 'Whiskey'
    elif letter == 'X':
        icao_name = 'X-ray'
    elif letter == 'Y':
        icao_name = 'Yankee'
    elif letter == 'Z':
        icao_name = 'Zulu'
    else:
        icao_name = '???'

    return icao_name                                             # Returning the ICAO word

# Function usage
name = input('Enter your name: ')                               # Reading the name from the keyboard
print('ICAO words for spelling out your name:')

for char in name:                                               # Going through each character in the name
    word = icao(char)                                           # Converting the character into an ICAO word
    print(word, end=" ")                                        # Printing the word on the same line

# 6. Function that converts time into 24-hour or 12-hour format======================================================================================================================================================================

def time_string(hours, minutes, time_format):                  # Defining a function
    if time_format == '24':                                    # Checking for 24-hour format
        result = f'{hours:02d}:{minutes:02d}'                  # Formatting hours and minutes
    else:                                                      # Using 12-hour format
        if hours == 0:                                         # Checking midnight
            hours = 12
            period = 'am'
        elif hours < 12:                                       # Checking morning hours
            period = 'am'
        elif hours == 12:                                      # Checking noon
            period = 'pm'
        else:                                                  # Checking afternoon and evening
            hours = hours - 12
            period = 'pm'

        result = f'{hours}:{minutes:02d}{period}'              # Creating the final time string

    return result                                              # Returning the time string

# Function usage
print(time_string(15, 38, '24'))
print(time_string(8, 3, '24'))
print(time_string(0, 5, '24'))
print(time_string(11, 15, '12'))
print(time_string(0, 7, '12'))
print(time_string(7, 30, '12'))
print(time_string(12, 46, '12'))
print(time_string(13, 10, '12'))
print(time_string(19, 2, '12'))
