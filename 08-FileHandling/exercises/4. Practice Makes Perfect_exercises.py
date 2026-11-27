# program that displays the first five lines from the it_company.csv file========================================================================================================================================================

file_name = 'it_company.csv'

counter = 0

with open(file_name, 'r') as file:
    for line in file:

        # Wyświetlamy kolejną linię
        print(line, end='')

        counter += 1

        # Po każdych pięciu liniach czekamy na Enter
        if counter % 5 == 0:
            input('\nPress Enter key...')

# program that uses regular expressions to fetch and print========================================================================================================================================================

import emails

# Odczytujemy zawartość pliku
with open('email.txt', 'r', encoding='utf-8') as file:
    email = file.read()

# Wyświetlamy informacje o wiadomości
print('Sender:', emails.email_sender(email))
print('Recipient:', emails.email_recipient(email))
print('Subject:', emails.email_subject(email))
print('Body:')
print(emails.email_body(email))

# program that calculates the number of lines, characters and words for any text file========================================================================================================================================================

file_name = input('File name: ')

try:

    # Odczytujemy całą zawartość pliku
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()

    # Obliczamy liczbę linii
    number_of_lines = len(content.splitlines())

    # Obliczamy liczbę znaków
    number_of_characters = len(content)

    # Obliczamy liczbę słów
    number_of_words = len(content.split())

    print('Number of lines:', number_of_lines)
    print('Number of characters:', number_of_characters)
    print('Number of words:', number_of_words)

except FileNotFoundError:
    print('File not found.')

# program that calculates the number of vowels in the text entered========================================================================================================================================================

import re

text = input('Enter text: ')

# Wzorzec zawierający angielskie samogłoski
pattern = r'[aeiouAEIOU]'

# Znajdujemy wszystkie samogłoski
vowels = re.findall(pattern, text)

# Obliczamy liczbę znalezionych samogłosek
counter = len(vowels)

print('Number of vowels:', counter)

# program that prints only those file names whose extensions consist of exactly four characters========================================================================================================================================================

import re

file_name = 'files.txt'

# Wzorzec rozszerzenia zawierającego dokładnie 4 litery
pattern = r'\.[a-z]{4}$'

# Otwieramy plik w trybie odczytu
with open(file_name, 'r') as file:
    for line in file:

        # Usuwamy znak nowej linii
        name = line.strip()

        # Sprawdzamy, czy rozszerzenie pasuje do wzorca
        if re.search(pattern, name):
            print(name)

# program that, based on the it_company.csv file, prints========================================================================================================================================================

import csv

file_name = 'it_company.csv'

print('GRAPHIC DESIGNERS')
print('=================')

# Otwieramy plik CSV
with open(file_name, 'r', encoding='utf-8') as file:

    # Odczytujemy dane według nazw kolumn
    reader = csv.DictReader(file)

    for row in reader:

        # Sprawdzamy stanowisko pracownika
        if row['Job Title'] == 'Graphic Designer':

            # Wyświetlamy imię, nazwisko i adres e-mail
            print(f"{row['First Name']} {row['Last Name']},{row['Email']}")


# program that prints those products whose price is less than 60 and whose stock is less than 40========================================================================================================================================================

import csv

file_name = 'clothing.csv'

# Otwieramy plik CSV
with open(file_name, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    for row in reader:

        # Zamieniamy dane tekstowe na liczby
        price = float(row['Price'])
        stock = int(row['Stock_Quantity'])

        # Sprawdzamy oba warunki
        if price < 60 and stock < 40:

            # Wyświetlamy wszystkie dane produktu
            print(','.join(row.values()))


# program that calculates, prints, and saves to a text file integers from 1 to 100 and their second and third powers========================================================================================================================================================

file_name = 'powers.txt'

with open(file_name, 'w') as file:

    # Przechodzimy przez liczby od 1 do 100
    for number in range(1, 101):

        # Obliczamy drugą i trzecią potęgę
        second_power = number ** 2
        third_power = number ** 3

        # Tworzymy linię tekstu
        line = f'{number},{second_power},{third_power}'

        # Wyświetlamy linię
        print(line)

        # Zapisujemy linię do pliku
        file.write(line + '\n')


# program that copies the book data from a given genre to its corresponding file========================================================================================================================================================

import csv


# Funkcja odczytująca książki z pliku CSV
def read_books(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        books = list(reader)

    return books


# Funkcja zapisująca książki wybranego gatunku
def save_books(books, genre, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for book in books:

            # Sprawdzamy gatunek książki
            if book['Genre'] == genre:

                # Łączymy dane książki przecinkami
                line = ','.join(book.values())

                # Zapisujemy książkę do pliku
                file.write(line + '\n')


# Odczytujemy wszystkie książki
books = read_books('books.csv')

# Zapisujemy książki według gatunków
save_books(books, 'Fantasy', 'books_fantasy.txt')
save_books(books, 'Historical', 'books_historical.txt')
save_books(books, 'Romance', 'books_romance.txt')
save_books(books, 'Classic', 'books_classic.txt')

print('Books saved successfully.')