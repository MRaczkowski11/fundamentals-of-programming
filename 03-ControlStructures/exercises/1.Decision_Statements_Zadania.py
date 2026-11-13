# Program to check if a person is an adult or not based on their age======================================================================================================================================================================

age = 16

if age >= 18:
    print("You are an adult")
else:
    print("You are under 18")

# Program checking if a car is exceeding the speed limit======================================================================================================================================================================

speed_limit = 140
car_speed = int(input('Enter car speed (km/h): '))

if car_speed > speed_limit:
    print(f'Your speed is {car_speed}km/h')
    print('Warning: speed limit exceeded!!')

# Program to check if a person has enough funds to make a payment======================================================================================================================================================================

account_balance = 500
total_payment = float(input('Enter total payment: '))

if total_payment <= account_balance:
    print('Payment completed')
else:
    print('No funds')

# payment = 140, Payment completed
# payment = 499, Payment completed
# payment = 500, Payment completed
# payment = 501, No funds
# payment = 720, No funds

# Program to check if a student passed a test based on the number of correctly completed tasks======================================================================================================================================================================

total_tasks = 20
tasks_ok = int(input('Enter number of correctly completed tasks: '))
test_passed = False

if tasks_ok / total_tasks >= 0.5:
    test_passed = True

if test_passed:
    print('Congratulations! You passed the test.')
else:
    print('Unfortunately, you failed the test.')

# score = 20, Congratulations! You passed the test.
# score = 11, Congratulations! You passed the test.
# score = 10, Congratulations! You passed the test.
# score = 9, Unfortunately, you failed the test.
# score = 0, Unfortunately, you failed the test.

# Program to check if a number is even or odd======================================================================================================================================================================

number = int(input('Enter number: '))

if number % 2 == 0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')

# Program to calculate the total salary of an employee based on their basic salary and whether they receive a bonus======================================================================================================================================================================

basic_salary = 5000
total_salary = 0
bonus = 0.30 # 30%

is_bonus = input('Does the employee receive a bonus? (Y/N): ') == 'Y'

if is_bonus:
    total_salary = basic_salary + basic_salary * bonus
else:
    total_salary = basic_salary

print(f'Basic salary: {basic_salary} PLN')
print(f'Bonus included? {is_bonus}')
print(f'Total salary: {total_salary:.2f} PLN')