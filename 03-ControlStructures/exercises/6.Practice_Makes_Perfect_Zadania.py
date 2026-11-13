# Program counts vowels in the text==================================================================================================================================================================================================

text = "This is a sample text."
vowels = "aeiouAEIOU"
vowel_count = 0

i = 0

while i < len(text):
    char = text[i]

    if char in vowels:
        vowel_count += 1

    i += 1

print(f"The number of vowels in the text is: {vowel_count}")

# Program checking how many bulbs are illuminating the house==================================================================================================================================================================================================

light_switch1 = False  # False - switch off, True - switch on
light_switch2 = False

bulbs_on = 0

if light_switch1:
    bulbs_on += 1

if light_switch2:
    bulbs_on += 2

print(f"Number of bulbs on: {bulbs_on}")

# Program password validator==================================================================================================================================================================================================

new_password = input('Enter new password: ')

if len(new_password) < 12:
    print('Password too short (min. 12 chars)')
else:
    print('Password is valid')

# Program that simulates the operation of an electronic thermometer==================================================================================================================================================================================================

temperature = 32

print(f"Temperature: {temperature}°C")

if temperature > 35:
    print("It is extremely hot")
elif temperature > 30:
    print("It is hot")
elif temperature >= 15:
    print("It is warm")
elif temperature >= 0:
    print("It is cold")
else:
    print("Warning, frost")

# Program calculates parking fee based on the number of hours parked==================================================================================================================================================================================================

hours = int(input("Enter the number of parking hours: "))

if hours >= 1 and hours <= 2:
    fee = 5
elif hours >= 3 and hours <= 6:
    fee = 15
elif hours > 6:
    fee = 20
else:
    fee = 0

print(f"Parking fee: {fee} PLN")

# Program checks which age group the user belongs to==================================================================================================================================================================================================

age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif age <= 19:
    print("Teen")
elif age <= 64:
    print("Adult")
else:
    print("Senior")

# Program checking if both people are adults==================================================================================================================================================================================================

person1_name = input('Enter first person name: ')
person1_age = int(input('Enter first person age: '))

person2_name = input('Enter second person name: ')
person2_age = int(input('Enter second person age: '))

if person1_age >= 18 and person2_age >= 18:
    print(f'Both {person1_name} and {person2_name} are adults')
else:
    print(f'Either {person1_name} or {person2_name} is not an adult')

# Program checks if a name is a Polish female name==================================================================================================================================================================================================

name = input('Enter name: ')

if name[-1].lower() == 'a':
    print(f'{name} -- Polish female name')

# Program calculates a dog's age in dog's years==================================================================================================================================================================================================

age = int(input("Enter the dog's age in human years: "))

if age <= 2:
    dog_age = age * 10.5
else:
    dog_age = 2 * 10.5 + (age - 2) * 4

print(f"The dog's age in dog's years is {dog_age:g} years.")

# Program analyses the price of a product in an online store==================================================================================================================================================================================================

current_price = 140.00
previous_price = 200.00

print(f"Current product price: {current_price:.2f}")
print(f"Previous product price: {previous_price:.2f}")

price_reduction = (previous_price - current_price) / previous_price * 100

if price_reduction >= 10:
    print("Buy the product!!")
    print(f"Product price reduced by {price_reduction:.0f}%")

# Program calculates the amount to pay after applying a discount==================================================================================================================================================================================================

number_of_products = int(input("Number of products purchased: "))
product_price = float(input("Product price: "))

if number_of_products > 2:
    amount_to_pay = 2 * product_price + (number_of_products - 2) * product_price * 0.75
else:
    amount_to_pay = number_of_products * product_price

print(f"Amount to pay: {amount_to_pay:.2f}")

# Program checks whether the car speed is within the valid range==================================================================================================================================================================================================


speed_limit_min = 40
speed_limit_max = 140

car_speed = int(input("Enter car speed: "))

if car_speed < speed_limit_min or car_speed > speed_limit_max:
    print("Warning: invalid car speed!!")

# Program checks whether a person is a good influencer==================================================================================================================================================================================================

facebook = True
twitter = False
instagram = True

if (facebook and twitter) or (facebook and instagram) or (twitter and instagram):
    print("You are a good influencer!")
else:
    print("You are not a good influencer.")

# Program checks whether an EAN-13 article number is correct==================================================================================================================================================================================================

ean = input("Enter EAN-13 article number: ")

if len(ean) == 13 and ean.isdigit():
    print("Article number is correct")

    if ean[:3] == "590":
        print("Article manufactured in Poland")

# Program calculates and prints the total washing time==================================================================================================================================================================================================

total_washing_time = 0

program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes: ')
extra_rinse = input('Extra rinse? (y/n): ')
extra_spin = input('Extra spin? (y/n): ')

if program == 'j':
    total_washing_time += 40
elif program == 'u':
    total_washing_time += 70
elif program == 's':
    total_washing_time += 20

if extra_rinse == 'y':
    total_washing_time += 15

if extra_spin == 'y':
    total_washing_time += 9

print(f'Total washing time: {total_washing_time} minutes')

# Program converts time from 24-hour format to 12-hour format==================================================================================================================================================================================================

time_24 = input('Enter time (24-hour format): ')

hours = int(time_24[:2])
minutes = time_24[3:5]

if hours >= 12:
    period = 'pm'
else:
    period = 'am'

if hours > 12:
    hours -= 12
elif hours == 0:
    hours = 12

print(f'Time in 12-hour format: {hours}:{minutes}{period}')

# Program determines the position of a point in the coordinate system==================================================================================================================================================================================================

x = float(input('Enter x coordinate: '))
y = float(input('Enter y coordinate: '))

if x > 0 and y > 0:
    print(f'Point P({x:g},{y:g}) is in the first quadrant of the coordinate system')
elif x < 0 and y > 0:
    print(f'Point P({x:g},{y:g}) is in the second quadrant of the coordinate system')
elif x < 0 and y < 0:
    print(f'Point P({x:g},{y:g}) is in the third quadrant of the coordinate system')
elif x > 0 and y < 0:
    print(f'Point P({x:g},{y:g}) is in the fourth quadrant of the coordinate system')
elif x == 0 and y == 0:
    print(f'Point P({x:g},{y:g}) is at the origin of the coordinate system')
elif x == 0:
    print(f'Point P({x:g},{y:g}) is on the y-axis')
else:
    print(f'Point P({x:g},{y:g}) is on the x-axis')

# Program survey with three yes-no questions==================================================================================================================================================================================================

print("SURVEY")

interested = input("Are you interested in computer science? (y/n): ") == 'y'
computer_games = input("Do you like playing computer games? (y/n): ") == 'y'
instagram = input("Do you have an Instagram account? (y/n): ") == 'y'

print()
print("SURVEY RESULTS")

print(f"Interested in computer science: {'Yes' if interested else 'No'}")
print(f"Playing computer games: {'Yes' if computer_games else 'No'}")
print(f"Has an Instagram account: {'Yes' if instagram else 'No'}")

# Program converts a decimal number into a binary number==================================================================================================================================================================================================

number = int(input('Enter decimal number: '))

decimal_number = number
binary_number = ''

if number == 0:
    binary_number = '0'
else:
    while number > 0:
        remainder = number % 2
        binary_number = str(remainder) + binary_number
        number = number // 2

print(f'{decimal_number}(10) = {binary_number}(2)')

# Program shows an amount of money using as few coins as possible==================================================================================================================================================================================================

amount = int(input('Enter the amount in PLN: '))

coins_5 = amount // 5
amount = amount % 5

coins_2 = amount // 2
amount = amount % 2

coins_1 = amount

print(f'The amount of PLN {coins_5 * 5 + coins_2 * 2 + coins_1} in coins:')
print(f'5 PLN coins: {coins_5}')
print(f'2 PLN coins: {coins_2}')
print(f'1 PLN coins: {coins_1}')

# Program prints numbers from 1 to 30 with special words==================================================================================================================================================================================================

for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print('BINGO', end=' ')
    elif i % 3 == 0:
        print('THREE', end=' ')
    elif i % 5 == 0:
        print('FIVE', end=' ')
    else:
        print(i, end=' ')

# Program creates a multiplication table for a given number==================================================================================================================================================================================================

number = int(input('Enter number: '))

for i in range(1, 11):
    print(f'{number} x {i} = {number * i}')

# Program Prints a triangle pattern==================================================================================================================================================================================================

for i in range(1, 6):
    print('* ' * i)

for i in range(4, 0, -1):
    print('* ' * i)

# Program prints a number pattern==================================================================================================================================================================================================

for i in range(1, 10):
    print(str(i) * i)

# Program checks whether the entered PIN code is correct==================================================================================================================================================================================================

correct_pin = '0805'
attempts = 0

while attempts < 3:
    pin = input('Enter the PIN code: ')

    if pin == correct_pin:
        print('PIN code is correct')
        break
    else:
        print('Incorrect')
        attempts += 1

if attempts == 3:
    print('Sorry, your payment card has been blocked.')

# Program prints the numeric keyboard using while loops==================================================================================================================================================================================================

i = 6

while i >= 0:
    j = 1

    while j <= 3:
        print(f'{i+j}', end=' ')
        j += 1

    print()
    i -= 3

# Program prints the first twenty numbers of the Fibonacci sequence==================================================================================================================================================================================================

a = 0
b = 1

for i in range(20):
    print(a, end=' ')

    next_number = a + b
    a = b
    b = next_number

# Program finds the first N prime numbers==================================================================================================================================================================================================

n = int(input('Enter the number of prime numbers: '))

print('Prime numbers:', end=' ')

number = 2
found = 0

while found < n:
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(number, end=' ')
        found += 1

    number += 1

# Program prints a lottery coupon with numbers from 1 to 49==================================================================================================================================================================================================

for i in range(1, 8):
    for j in range(7):
        print(i + j * 7, end=' ')
    print()

# Program prints 20 random integers in the range of 5 to 10==================================================================================================================================================================================================

import random

for i in range(20):
    print(random.randint(5, 10), end=' ')