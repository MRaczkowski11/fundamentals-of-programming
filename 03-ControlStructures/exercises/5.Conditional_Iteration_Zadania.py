# Program running while loop============================================================================================================================================================================================================

count = 0

while count < 5:
    print(count)
    count += 1

# Program prints a greeting============================================================================================================================================================================================================

name = ''

while name == '':
    name = input('Enter your name: ')

print(f'Hello {name}')

# A simple number guessing game=========================================================================================================================================================================================================

import random

number_to_guess = random.randint(1, 100)
user_guess = 0

print("Guess the number between 1 and 100!")

while user_guess != number_to_guess:
    user_guess = int(input("Enter your guess: "))

    if user_guess < number_to_guess:
        print("Too low! Try again.")
    elif user_guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the correct number.")

# Program sums numbers entered by user and calculates their arithmetic mean============================================================================================================================================================

total_sum = 0
count = 0

while True:
    number = int(input("Enter a number (0 to stop): "))

    if number == 0:
        break                        # Exit the loop when 0 is entered

    total_sum += number
    count += 1

print(f"The total sum of the numbers is: {total_sum}")

if count > 0:
    average = total_sum / count
    print(f"The arithmetic mean is: {average}")
else:
    print("No numbers were entered.")

# Program calculates the sum of even numbers from 1 to a given number N================================================================================================================================================================

N = 10
sum_even = 0
i = 1

while i <= N:
    if i % 2 == 0:
        sum_even += i

    i += 1

print(f"The sum of even numbers from 1 to {N} is: {sum_even}")

# Program takes a number from the user and counts down to zero==========================================================================================================================================================================

import time

countdown = int(input("Enter the number of seconds to count down: "))

numbers_in_words = {
    5: 'five',
    4: 'four',
    3: 'three',
    2: 'two',
    1: 'one'
}

while countdown > 0:
    if countdown <= 5:
        print(numbers_in_words[countdown])
    else:
        print(countdown)

    countdown -= 1
    time.sleep(1)           # Wait for 1 second

print("Time's up!")

# Program ATM (cash machine) simulator=================================================================================================================================================================================================

balance = 1000  # Initial balance
pin = '1111'  # Initial 4-digit PIN code

while True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check PIN")
    print("5. Change PIN")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")
    print()

    if choice == '1':
        print(f"Your current balance is: €{balance}")

    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")

    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance.")

    elif choice == '4':
        entered_pin = input("Enter your PIN: ")

        if entered_pin == pin:
            print("Correct PIN!")
        else:
            print("Incorrect PIN.")

    elif choice == '5':
        current_pin = input("Enter your current PIN: ")

        if current_pin == pin:
            new_pin = input("Enter your new 4-digit PIN: ")

            if len(new_pin) == 4 and new_pin.isdigit():
                confirm_pin = input("Confirm your new PIN: ")

                if new_pin == confirm_pin:
                    pin = new_pin
                    print("PIN successfully changed.")
                else:
                    print("PINs do not match.")
            else:
                print("Invalid PIN. It must contain exactly 4 digits.")
        else:
            print("Incorrect current PIN.")

    elif choice == '6':
        print("Exiting... Thank you for using the ATM!")
        break  # Exit the loop

    else:
        print("Invalid option. Please try again.")