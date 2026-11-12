# Program obliczający ilość znaków w stringu========================================================================================================================================================================================================

name = 'Mateusz'
surname = 'Raczkowski'

characters_in_name = len(name)
characters_in_surname = len(surname)
characters_in_full_name = len(name + ' ' + surname)

print(f'Your name has {characters_in_name} characters')
print(f'Your surname has {characters_in_surname} characters')
print(f'Your full name has {characters_in_full_name} characters')

# Your name has 7 characters
# Your surname has 11 characters
# Your full name has 17 characters

# Program piszący inicjały imienia i nazwiska========================================================================================================================================================================================================

name = 'Mateusz'
surname = 'Raczkowski'

print(name[0])
print(surname[0])

# M
# R

# Program piszący skrót uniwersytetu========================================================================================================================================================================================================

university = "Krakow University of Economics"

abbreviation = university[7] + university[17] + university[0]

print(abbreviation)

# UEK

# Program piszący informacje========================================================================================================================================================================================================

employee = "Mr. John May, born on 1998-02-16"

print(f'Name: {employee[4:8]}')
print(f'Surname: {employee[9:12]}')
print(f'Born: {employee[23:33]}')
print(f'Initials: {employee[4]}{employee[9]}')

# program piszący numer telefonu========================================================================================================================================================================================================

phone = input('Enter phone number: ')

formatted_phone = phone[:3] + '-' + phone[3:6] + '-' + phone[6:9]

print(f'Phone number: {formatted_phone}')

# Program piszący numery odpowiadające literom========================================================================================================================================================================================================

print(f'a {ord("a")}')
print(f'b {ord("b")}')
print(f'z {ord("z")}')
print(f'A {ord("A")}')
print(f'B {ord("B")}')
print(f'Z {ord("Z")}')
print(f'1 {ord("1")}')
print(f'= {ord("=")}')
print(f'+ {ord("+")}')
print(f'€ {ord("€")}')

# a 97
# b 98 
# z 122
# A 65
# B 66
# Z 90
# 1 49
# = 61
# + 43
# € 8364

# Program piszący numery odpowiadające literom w imieniu========================================================================================================================================================================================================

name = 'Mateusz'

print(f'The letter {name[0]} has a code {ord(name[0])}')
print(f'The letter {name[1]} has a code {ord(name[1])}')
print(f'The letter {name[2]} has a code {ord(name[2])}')
print(f'The letter {name[3]} has a code {ord(name[3])}')
print(f'The letter {name[4]} has a code {ord(name[4])}')
print(f'The letter {name[5]} has a code {ord(name[5])}')
print(f'The letter {name[6]} has a code {ord(name[6])}')

# The letter M has a code 77
# The letter a has a code 97
# The letter t has a code 116
# The letter e has a code 101
# The letter u has a code 117
# The letter s has a code 115
# The letter z has a code 122

# Program obliczający ile liter znajduje się pomiedzy literami w imieniu========================================================================================================================================================================================================

first = input('Enter first letter: ')
last = input('Enter last letter: ')

first_letter_code = ord(first)
last_letter_code = ord(last)

number_of_letters = max(0, abs(last_letter_code - first_letter_code) - 1)               # Obliczanie ilości liter znajdujących się pomiędzy literami w imieniu poprzez obliczenie różnicy kodów ASCII liter i odjęcie 1

print(f'Between {first} and {last} is {number_of_letters} letters')

# Program piszący słowo z liczb odpowiadających literom========================================================================================================================================================================================================

print(chr(67), chr(111), chr(111), chr(108), chr(33))

# C o o l !

# String manipulation========================================================================================================================================================================================================

movie = "The Lord of the Rings: The Return of the King"

print('Number of characters: ', len(movie))               # Obliczanie ilości znaków w stringu movie z użyciem funkcji len()

print('Uppercase: ', movie.upper())                      # Konwersja stringu movie na wielkie litery z użyciem metody upper()

print('Lowercase: ', movie.lower())                     # Konwersja stringu movie na małe litery z użyciem metody lower()

print('Number of e characters: ', movie.count('e'))            # Obliczanie ilości wystąpień litery 'e' w stringu movie z użyciem metody count()

print('Position of Lord: ', movie.find('Lord'))                 # Znajdowanie pozycji pierwszego wystąpienia słowa 'Lord' w stringu movie z użyciem metody find()

print('Position of dragon: ', movie.find('dragon'))      