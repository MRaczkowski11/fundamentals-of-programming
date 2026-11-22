# 1. Program that prints the name of a month======================================================================================================================================================================

import months                                                   # Importing the months module

month_number = int(input('Enter month number: '))              # Reading the month number
month_name = months.month(month_number)                        # Getting the month name

print(f'The name of month {month_number} is {month_name}')

# 2. Program that counts the number of letter 'e' in a sentence======================================================================================================================================================================

import letter_counter                                         # Importing the module

text = 'You never get a second chance to make a first impression'

result = letter_counter.count_letter(text, 'e')               # Counting the letter 'e'

print(text)
print("The number of letter 'e':", result)

# 3. Program that checks if a number is within a given range======================================================================================================================================================================

import number_range                                            # Importing the module

number = int(input('A number: '))                              # Reading a number
result = number_range.in_range(number, 2, 15)                  # Checking the range

print(f'Number {number} in the range <2,15>: {result}')

# 4. Program that hides credit card number digits======================================================================================================================================================================

import card                                                    # Importing the card module

card_number = "5290312400019022"                               # Credit card number
hidden_number = card.hide(card_number)                        # Hiding the card number

print(hidden_number)

# 5. Function that checks if a string is a valid binary number======================================================================================================================================================================

def f(binary_number):                                          # Defining a function
    for digit in binary_number:                                # Going through each character
        if digit != '0' and digit != '1':                      # Checking if the character is not 0 or 1
            return False                                       # Returning False if invalid

    return True                                                # Returning True if all characters are valid

# Function usage
print(f("101101"))
print(f("1311a10100"))

# 6. Function that calculates the minimum number of coins======================================================================================================================================================================

def f(amount_to_pay):                                          # Defining a function
    coins = 0                                                  # Initializing the number of coins

    while amount_to_pay >= 5:                                  # Using 5 PLN coins
        amount_to_pay = amount_to_pay - 5
        coins = coins + 1

    while amount_to_pay >= 2:                                  # Using 2 PLN coins
        amount_to_pay = amount_to_pay - 2
        coins = coins + 1

    while amount_to_pay >= 1:                                  # Using 1 PLN coins
        amount_to_pay = amount_to_pay - 1
        coins = coins + 1

    return coins                                               # Returning the number of coins

# Function usage
print(f(23))
print(f(8))
print(f(2))
print(f(0))

# 7. Function that calculates the sum of even or odd digits======================================================================================================================================================================

def f(number, even):                                           # Defining a function
    number = abs(number)                                       # Converting the number to its absolute value
    number_string = str(number)                                # Converting the number to a string
    total = 0                                                  # Initializing the sum

    for digit in number_string:                                # Going through each digit
        digit = int(digit)                                     # Converting the character into an integer

        if even == True and digit % 2 == 0:                    # Checking for even digits
            total = total + digit
        elif even == False and digit % 2 != 0:                 # Checking for odd digits
            total = total + digit

    return total                                               # Returning the sum

# Function usage
print(f(3124, True))
print(f(3124, False))
print(f(20576, False))
print(f(20576, True))
print(f(13115, True))

# 8. Function that counts negative even numbers in a given range======================================================================================================================================================================

def f(x, y):                                                   # Defining a function
    counter = 0                                                # Initializing the counter

    for number in range(x, y + 1):                             # Going through numbers from x to y
        if number < 0 and number % 2 == 0:                     # Checking if the number is negative and even
            counter = counter + 1                              # Increasing the counter

    return counter                                             # Returning the number of negative even numbers

# Function usage
print(f(-7, 8))
print(f(-1, 11))

# 9. Function that checks if at least one number is negative======================================================================================================================================================================

def f(n1, n2, n3):                                             # Defining a function
    if n1 < 0 or n2 < 0 or n3 < 0:                            # Checking if at least one number is negative
        return True
    else:
        return False

# Function usage
print(f(11, 6, -4))
print(f(5, 4, 14))


# 10. Function that returns a string of asterisks separated by slashes======================================================================================================================================================================

def f(n):                                                      # Defining a function
    result = ''                                                # Initializing the result

    for i in range(n):                                        # Repeating n times
        if i > 0:                                              # Checking if this is not the first asterisk
            result = result + '/'
        result = result + '*'                                  # Adding an asterisk

    return result                                              # Returning the result

# Function usage
print(f(4))
print(f(1))


# 11. Function that returns numbers from 1 to n as a string======================================================================================================================================================================

def f(n):                                                      # Defining a function
    result = ''                                                # Initializing the result

    for number in range(1, n + 1):                             # Going through numbers from 1 to n
        result = result + str(number)                          # Converting the number to a string and adding it

    return result                                              # Returning the result

# Function usage
print(f(11))
print(f(4))

# 12. Function that performs an arithmetic operation======================================================================================================================================================================

def f(number1, number2, operator):                             # Defining a function
    if operator == '+':                                        # Addition
        result = number1 + number2
    elif operator == '-':                                      # Subtraction
        result = number1 - number2
    elif operator == '*':                                      # Multiplication
        result = number1 * number2
    elif operator == '%':                                      # Modulo
        result = number1 % number2
    elif operator == '**':                                     # Exponentiation
        result = number1 ** number2
    else:
        result = 'Invalid operator'

    return result                                              # Returning the result

# Function usage
print(f(2, 3, "+"))
print(f(2, 3, "%"))
print(f(2, 3, "**"))
print(f(2, 3, "*"))
print(f(2, 3, "-"))

# 13. Function that checks if at least 3 people were in the room at the same time======================================================================================================================================================================

def f(detector):                                               # Defining a function
    people = 0                                                 # Initializing the number of people

    for symbol in detector:                                    # Going through each detector symbol
        if symbol == '+':                                      # Checking if someone entered
            people = people + 1
        elif symbol == '-':                                    # Checking if someone left
            people = people - 1

        if people >= 3:                                        # Checking if at least 3 people are inside
            return True

    return False                                               # Returning False if there were never 3 people

# Function usage
print(f("+-+++-+---"))
print(f("+-+-+-+-"))
print(f("+-++-+--"))
print(f("+-++-++-+---"))

# 14. Function that returns the n-th value of the Fibonacci sequence======================================================================================================================================================================

def f(n):                                                      # Defining a function
    if n == 1:                                                 # Checking the first value
        return 0
    elif n == 2:                                               # Checking the second value
        return 1

    a = 0                                                     # First Fibonacci number
    b = 1                                                     # Second Fibonacci number

    for i in range(3, n + 1):                                  # Calculating the next numbers
        c = a + b                                              # Adding the previous two numbers
        a = b                                                   # Moving the second number to the first position
        b = c                                                   # Saving the new Fibonacci number

    return b                                                   # Returning the n-th value

# Function usage
print(f(5))
print(f(9))

# 15. Function that checks if a text is a palindrome======================================================================================================================================================================

def f(palindrome):                                             # Defining a function
    if palindrome == palindrome[::-1]:                        # Comparing the text with its reverse
        return True
    else:
        return False

# Function usage
print(f("radar"))
print(f("12-11-21"))
print(f("book"))

# 16. Function that removes spaces from a sentence======================================================================================================================================================================

def f(sentence):                                               # Defining a function
    result = sentence.replace(' ', '')                        # Replacing spaces with empty strings
    return result                                              # Returning the result

# Function usage
print(f("integrated development environment"))
print(f("A programming language is a system of notation for writing computer programs"))

# 17. Function that calculates the sum of repeated digits in a number======================================================================================================================================================================

def f(number):                                                 # Defining a function
    number_string = str(number)                                # Converting the number to a string
    total = 0                                                  # Initializing the sum

    for digit in number_string:                                # Going through each digit
        if number_string.count(digit) > 1:                     # Checking if the digit appears more than once
            total = total + int(digit)                         # Adding the repeated digit to the sum

    return total                                               # Returning the sum

# Function usage
print(f(1027))
print(f(230335))
print(f(513553007))

# 18. Function that returns the n-th prime number======================================================================================================================================================================

def f(n):                                                      # Defining a function
    counter = 0                                                # Counting prime numbers
    number = 1                                                 # Starting number

    while counter < n:                                         # Repeating until n prime numbers are found
        number = number + 1                                    # Checking the next number
        is_prime = True                                        # Assuming the number is prime

        for i in range(2, number):                             # Checking possible divisors
            if number % i == 0:                                # Checking if the number is divisible
                is_prime = False
                break

        if is_prime == True:                                   # Checking if the number is prime
            counter = counter + 1                              # Increasing the counter

    return number                                              # Returning the n-th prime number

# 19. Function that returns the difference between the largest and smallest numbers======================================================================================================================================================================

def f(number1, number2, number3):                              # Defining a function
    largest = max(number1, number2, number3)                   # Finding the largest number
    smallest = min(number1, number2, number3)                  # Finding the smallest number

    result = largest - smallest                               # Calculating the difference

    return result                                              # Returning the result

# Function usage
print(f(7, 4, 9))
print(f(2, 12, 8))

# 20. Function that returns an acronym from a text======================================================================================================================================================================

def f(name):                                                   # Defining a function
    words = name.split()                                      # Splitting the text into words
    result = ''                                                # Initializing the result

    for word in words:                                         # Going through each word
        result = result + word[0]                              # Adding the first letter of the word

    return result                                              # Returning the acronym

# Function usage
print(f("Internet of Things"))
print(f("For Your Information"))
print(f("Python"))

# 21. Function that checks if a password is valid======================================================================================================================================================================

def f(password):                                               # Defining a function
    if len(password) < 6:                                      # Checking if password has at least 6 characters
        return False

    for char in password:                                      # Going through each character
        if password.count(char) > 1:                           # Checking if a character appears more than once
            return False

    return True                                                # Returning True if password is valid

# Function usage
print(f("ax15"))
print(f("book123"))
print(f("A2water3"))
print(f("qwerty"))
print(f(""))

# 22. Function that calculates the value of an arithmetic expression======================================================================================================================================================================

def f(expression):                                             # Defining a function
    result = int(expression[0])                                # Getting the first number
    i = 1                                                       # Starting position in the expression

    while i < len(expression):                                 # Going through the expression
        operator = expression[i]                               # Reading the operator
        number = int(expression[i + 1])                        # Reading the next number

        if operator == '+':                                    # Checking for addition
            result = result + number
        elif operator == '-':                                  # Checking for subtraction
            result = result - number

        i = i + 2                                               # Moving to the next operator

    return result                                              # Returning the result

# Function usage
print(f("2+3"))
print(f("3+8+1"))
print(f("2+3-4+5-0"))

# 23. Function that calculates the sum of numbers divisible by 2 and 3 but not by 4======================================================================================================================================================================

def f(x, y):                                                   # Defining a function
    total = 0                                                  # Initializing the sum

    for number in range(x, y + 1):                             # Going through numbers from x to y
        if number % 2 == 0 and number % 3 == 0 and number % 4 != 0:
            total = total + number                             # Adding the number to the sum

    return total                                               # Returning the sum

# Function usage
print(f(1, 20))
print(f(10, 30))

# 24. Function that separates all characters with a dash======================================================================================================================================================================

def f(text):                                                   # Defining a function
    result = ''                                                # Initializing the result

    for i in range(len(text)):                                 # Going through each character
        if i > 0:                                               # Checking if this is not the first character
            result = result + '-'
        result = result + text[i]                              # Adding the character

    return result                                              # Returning the result

# Function usage
print(f("Univesity"))
print(f("UE"))
print(f("x"))
print(f(""))

# 25. Function that checks if a product code is correct======================================================================================================================================================================

def f(product_code):                                           # Defining a function
    if len(product_code) != 4:                                 # Checking if the code has four digits
        return False

    total = int(product_code[0]) + int(product_code[1]) + int(product_code[2])
    control_digit = total % 7                                  # Calculating the control digit

    if control_digit == int(product_code[3]):                  # Comparing the control digit
        return True
    else:
        return False

# Function usage
print(f("1082"))
print(f("2035"))
print(f("1114"))
print(f("7071"))

# 26. Function that finds the longest sequence of the same dice result======================================================================================================================================================================

def f(dice):                                                    # Defining a function
    longest = 1                                                 # Length of the longest sequence
    current = 1                                                 # Length of the current sequence
    result = dice[0]                                            # Initializing the result

    for i in range(1, len(dice)):                              # Going through the dice results
        if dice[i] == dice[i - 1]:                             # Checking if the current digit is the same as the previous
            current = current + 1
        else:
            current = 1                                         # Resetting the current sequence

        if current > longest:                                   # Checking if the sequence is the longest
            longest = current
            result = dice[i]                                    # Saving the dice result

    return int(result)                                          # Returning the most repeated dice result

# Function usage
print(f("5233165554211"))
print(f("2133"))

# 27. Function that calculates factorial using recursion======================================================================================================================================================================

def factorial(n):                                              # Defining a recursive function

    if n == 0 or n == 1:                                       # Base case: 0! = 1 and 1! = 1
        return 1

    if n > 1:                                                  # Checking if the number is greater than 1
        return n * factorial(n - 1)                            # Calling the function again

# Function usage
number = 5                                                     # Number for factorial calculation
result = factorial(number)                                     # Calculating the factorial

print(f'The factorial of {number} is {result}')

# 28. Function that calculates the sum of natural numbers using recursion======================================================================================================================================================================

def sum_natural(n):                                            # Defining a recursive function
    if n == 1:                                                 # Base case
        return 1

    return n + sum_natural(n - 1)                              # Adding n and calling the function again

# Function usage
result = sum_natural(10)                                       # Calculating the sum from 1 to 10

print('The sum of natural numbers from 1 to 10 is', result)

# 29. Function that calculates power using recursion======================================================================================================================================================================

def power(x, n):                                               # Defining a recursive function
    if n == 0:                                                 # Base case: any number to the power of 0 is 1
        return 1

    return x * power(x, n - 1)                                 # Multiplying x by the previous power

# Function usage
result = power(5, 3)                                           # Calculating 5 to the power of 3

print('5 to the power of 3 is', result)
