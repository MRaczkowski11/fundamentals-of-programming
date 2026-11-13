# Program prints the sentence "Practice makes perfect!" six times=========================================================================================================================================================================

for i in range(6):
    print('Practice makes perfect!')

# Program prints the name of university where you are studying with an extra space between characters====================================================================================================================================

university = 'Krakow University of Economics'
university_expanded = ''

for char in university:
    university_expanded = university_expanded + char + ' '

print(university)
print(university_expanded)

# Program encrypts text using Caesar Code, shifting each letter in the alphabet right one position=======================================================================================================================================

plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    
    char_code = ord(char)

    char_code = char_code + 1

    new_char = chr(char_code)

    encrypted_text = encrypted_text + new_char

print(plain_text)
print(encrypted_text)

# Program calculates the sum of integer numbers in the range <5,10>=======================================================================================================================================================================

sum = 0

for i in range(5, 11):
    sum += i

print(f'Sum is {sum}')

# Program calculates the sum of even numbers in the range <1,10>==========================================================================================================================================================================

sum = 0

for i in range(1, 11):
    if i % 2 != 0:
        continue
    sum += i

print(f'Sum of even numbers in the range <1,10> is {sum}')

# Program calculates values for the following fractions: 1/2, 1/3, ..., 1/10==============================================================================================================================================================

for i in range(1, 11):
    print(f'1/{i} = {1/i}')