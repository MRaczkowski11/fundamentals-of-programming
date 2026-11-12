# Program Ulgi od podatków========================================================================================================================================================================================================

age = int(input('Enter age: '))               # Pobieranie wieku od użytkownika i konwersja na typ int
no_tax = age <= 26

print(f'Exemption from paying taxes: {no_tax}')               # Wyświetlanie informacji o uldze od podatków

# Program Długości hasła========================================================================================================================================================================================================

password = input('Enter password: ')
password_ok = len(password) >= 8 

print(f'Password length is valid: {password_ok}')      

# Program który sprawdza czy liczba jest parzysta========================================================================================================================================================================================================

number = int(input('Enter number: '))
even = number % 2 == 0

print(f'Number is even: {even}')

# Program który sprawdza czy drzewo może być ścięte========================================================================================================================================================================================================

import math         

circumference = float(input('Enter tree circumference in cm: '))                # Obliczanie średnicy drzewa na podstawie podanego obwodu drzewa w centymetrach i sprawdzanie, czy drzewo może być ścięte (czy średnica jest większa lub równa 50 cm)

diameter = circumference / math.pi               # Obliczanie średnicy drzewa na podstawie podanego obwodu drzewa w centymetrach (średnica = obwód / π)
can_be_cut_down = diameter >= 50                 # Sprawdzanie, czy średnica drzewa jest większa lub równa 50 cm, co oznacza, że drzewo może być ścięte

print(f'Tree can be cut down: {can_be_cut_down}')

# Program który sprawdza czy rejestracja samochodu jest z Krakowa========================================================================================================================================================================================================

car_number = input('Enter car registration number: ')
is_krakow = car_number[0:2] == "KR" or car_number[0:2] == "KK"                     # Sprawdzanie, czy rejestracja samochodu zaczyna się od "KR" lub "KK", co oznacza, że samochód jest zarejestrowany w Krakowie

print(f'Car is from Krakow: {is_krakow}')

# Program sprawdza prędkość samochodu i wyświetla informację, czy kierowca przekroczył dozwoloną prędkość========================================================================================================================================================================================================

speed = int(input('Enter vehicle speed: '))
speed_valid = speed >= 40 and speed <= 140

print(f'Speed is valid: {speed_valid}')

# Program random()========================================================================================================================================================================================================

import random

random_number = random.randint(5, 10)
print(random_number)

# 7, 10, 5, 8, 6

#Program symuluje rzut trzema kostkami i oblicza sumę oczek z trzech rzutów========================================================================================================================================================================================================

import random

dice_roll_1 = random.randint(1, 6)
dice_roll_2 = random.randint(1, 6)
dice_roll_3 = random.randint(1, 6)

total = dice_roll_1 + dice_roll_2 + dice_roll_3

print(f'First dice: {dice_roll_1}')
print(f'Second dice: {dice_roll_2}')
print(f'Third dice: {dice_roll_3}')
print(f'Total: {total}')

# Program symuluje rzut kostką i sprawdza, czy wylosowana liczba jest specjalna (1 lub 6)========================================================================================================================================================================================================

import random

dice_roll = random.randint(1, 6)
special_number = dice_roll == 1 or dice_roll == 6

print(f'Dice rolled: {dice_roll}')
print(f'Special number (1 or 6): {special_number}')

# Program gry w zgadywanie liczby========================================================================================================================================================================================================

import random

computer = random.randint(1, 6)

you = int(input('Guess the dice number (1-6): '))

you_won = you == computer

print(f'Computer rolled: {computer}')
print(f'You won: {you_won}')