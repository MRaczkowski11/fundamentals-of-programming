# Program to check the temperature and print the corresponding weather condition==========================================================================================================================================================

temperature = 15

if temperature > 25:
    print('Hot')
elif temperature > 15:
    print('Warm')
elif temperature == 15:
    print('Mild')
else:
    print('Cold')

# Progrma to check the size symbol and print the corresponding size description===========================================================================================================================================================

size = input('Enter size symbol: ')

if size == 'S':
    print('S: Small size')
elif size == 'M':
    print('M: Medium size')
elif size == 'L':
    print('L: Large size')
elif size == 'XL':
    print('XL: Extra large size')
else:
    print('Incorrect symbol')


# Program to check fuel consumption based on driving mode=================================================================================================================================================================================

driving_mode = input('Enter driving mode (A/M/E): ')
distance = int(input('Enter distance in km: '))

if driving_mode == 'A':
    fuel_consumption = 7 
elif driving_mode == 'M':
    fuel_consumption = 9 
elif driving_mode == 'E':
    fuel_consumption = 6 
else:
    fuel_consumption = 0

total_consumption = distance / 100 * fuel_consumption

print(f'Total fuel consumption over a distance of {distance} km in driving mode {driving_mode} is {total_consumption} liters')

# Simple Calculator Program================================================================================================================================================================================================================

number1 = float(input('Enter first number: '))
number2 = float(input('Enter second number: '))
operator = input('Enter operator (+, -, *, /): ')

if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '*':
    result = number1 * number2
elif operator == '/':
    result = number1 / number2                     
else:
    result = 'Invalid operator'

print(f'{number1} {operator} {number2} = {result}') 
 
# 2 + 3 = 5
# 2 * 4 = 8
# 3 - 5 = -2
# 5 * 6 = 30

# Program that calculates and prints the quarter of the year for a given month===========================================================================================================================================================

month = int(input('Enter month number (1..12): '))

if month >= 10:
    quarter = 4
elif month >= 7:
    quarter = 3
elif month >= 4:
    quarter = 2
else:
    quarter = 1

print(f'Month {month} is in quarter {quarter}')

# Month = 12, Quarter = 4
# Month = 10, Quarter = 4
# Month = 9, Quarter = 3
# Month = 1, Quarter = 1

# Program that checks if a number is positive, negative or zero===========================================================================================================================================================================

number = int(input('Enter number: '))

if number > 0:
    print(f'Number {number} is positive')
elif number < 0:
    print(f'Number {number} is negative')
else:
    print('Number is 0')

# Number 7 is positive
# Number 1 is positive
# Number is 0
# Number -1 is negative
# Number -4 is negative


