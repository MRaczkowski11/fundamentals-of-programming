# Using Regular Expressions========================================================================================================================================================

#[A-Z][a-z]+ \d{1,2}, \d{4}

# March 12, 1992, June 5, 1988

# \d{3}-\d{3}-\d{4}

# 555-123-4567, 555-765-4321

# \b\d{1,3}(,\d{3})+\b

# 1,234, 1,235

# \b[A-Z][a-z]+\b

# Alice, John, Mike

# \b\d+\b

# (?<![\w,-])\d+(?![\w,-])

# program that calculates the total value of money spent========================================================================================================================================================

import re

email_file = 'report.txt'

# Odczytujemy zawartość wiadomości
with open(email_file, 'r', encoding='utf-8') as file:
    email = file.read()

# Wzorzec wyszukujący kwoty poprzedzone symbolem euro
pattern = r'€\s*(\d+(?:\.\d{1,2})?)'

# Pobieramy wszystkie znalezione kwoty
amounts = re.findall(pattern, email)

total = 0

# Zamieniamy znalezione napisy na liczby
for amount in amounts:
    total += float(amount)

print(f'Total purchases: €{total:.2f}')

# checks whether a username and password entered from the keyboard meet the requirements========================================================================================================================================================

import re

username = input('Enter username: ')
password = input('Enter password: ')

# Wzorzec dla nazwy użytkownika
username_pattern = r'^[a-z]{6,}$'

# Wzorzec dla hasła
password_pattern = r'^[a-zA-Z0-9_]{8,}$'

# Sprawdzamy zgodność ze wzorcami
username_match = re.match(username_pattern, username)
password_match = re.match(password_pattern, password)

# Oba warunki muszą zostać spełnione
if username_match and password_match:
    print('Username and password are correct.')
else:
    print('Invalid username or password.')

