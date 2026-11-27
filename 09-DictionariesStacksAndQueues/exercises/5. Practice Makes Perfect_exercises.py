# program to translate words from English to Polish========================================================================================================================================================

translations = {
    'computer': 'komputer',
    'mouse': 'myszka',
    'keyboard': 'klawiatura',
    'printer': 'drukarka'
}

word = input('Enter an English word: ')

# Sprawdzamy, czy słowo istnieje w słowniku
if word in translations:
    print('Translation:', translations[word])
else:
    print('Translation is unavailable.')

# program that calculates and prints the total number of hour========================================================================================================================================================

winter_semester = {
    'math': 60,
    'programming': 30,
    'history': 15
}

# Sumujemy wszystkie wartości słownika
total = sum(winter_semester.values())

print('The total number of hours in the winter semester is', total)

# program that counts how many times each word appears in a paragraph========================================================================================================================================================

paragraph = 'cat dog mouse cat rat cat mouse'

# Dzielimy tekst na pojedyncze słowa
words = paragraph.split()

# Tworzymy pusty słownik
word_count = {}

for word in words:

    # Jeżeli słowo już istnieje, zwiększamy licznik
    if word in word_count:
        word_count[word] += 1

    # Jeżeli słowa jeszcze nie ma, dodajemy je
    else:
        word_count[word] = 1

# Wyświetlamy słowa i liczbę ich wystąpień
for word, count in word_count.items():
    print(f'{word}: {count}')

# program that creates a dictionary called person containing data from the two other dictionaries========================================================================================================================================================

basic_data = {
    'name': 'Barbara',
    'age': 21
}

advanced_data = {
    'status': 'student',
    'married': False,
    'interest': ['reading', 'swimming']
}

# Łączymy oba słowniki
person = basic_data | advanced_data

# Wyświetlamy zawartość nowego słownika
for key, value in person.items():
    print(f'{key}: {value}')

# program that calculates and displays the average price for a room in hotels in Krakow and Sopot========================================================================================================================================================

hotels_in_Krakow = [
    {'name': 'Sky', 'price': 320.00},
    {'name': 'Metropol', 'price': 480.00},
    {'name': 'New Port', 'price': 420.00},
    {'name': 'Aparthotel', 'price': 390.00}
]

hotels_in_Sopot = [
    {'name': 'Focus', 'price': 510.00},
    {'name': 'Aqua', 'price': 345.00},
    {'name': 'La Boutique', 'price': 390.00},
    {'name': 'Marina', 'price': 410.00}
]


# Funkcja zwracająca nazwy hoteli oddzielone przecinkami
def hotel_list(hotels):
    names = []

    for hotel in hotels:
        names.append(hotel['name'])

    return ','.join(names)


# Funkcja obliczająca średnią cenę hotelu
def avg_price(hotels):
    total = 0

    for hotel in hotels:
        total += hotel['price']

    return round(total / len(hotels))


krakow_price = avg_price(hotels_in_Krakow)
sopot_price = avg_price(hotels_in_Sopot)

print('Hotels in Krakow:', hotel_list(hotels_in_Krakow))
print('Average hotel price in Krakow:', krakow_price)

print('Hotels in Sopot:', hotel_list(hotels_in_Sopot))
print('Average hotel price in Sopot:', sopot_price)

# Porównujemy średnie ceny
if krakow_price < sopot_price:
    print('Cheaper hotels in: Krakow')

elif sopot_price < krakow_price:
    print('Cheaper hotels in: Sopot')

else:
    print('Average prices are equal.')

# program to calculate the total cost of a shopping cart using a price list========================================================================================================================================================

# Cennik produktów
prices = {
    'milk': 1.49,
    'butter': 2.09,
    'juice': 1.19,
    'bread': 1.99
}

# Koszyk zawierający ilości produktów
cart = {
    'juice': 3,
    'bread': 1,
    'milk': 2
}

total = 0

# Mnożymy cenę produktu przez jego ilość
for product, quantity in cart.items():
    total += prices[product] * quantity

print(f'Total cost: {total:.2f}')

# program that calculates and prints how many registered cars come from each province of Poland========================================================================================================================================================

import csv

# Tworzymy dwa puste słowniki
provinces = {}
vehicle_count = {}

# Odczytujemy województwa i odpowiadające im litery
with open('province.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    for row in reader:
        letter = row['Letter']
        name = row['Name']

        provinces[letter] = name
        vehicle_count[letter] = 0

# Odczytujemy numery rejestracyjne
with open('vehicle.txt', 'r') as file:
    for line in file:

        # Usuwamy znak nowej linii
        registration = line.strip()

        # Pobieramy pierwszą literę rejestracji
        letter = registration[0]

        # Zwiększamy licznik danego województwa
        if letter in vehicle_count:
            vehicle_count[letter] += 1

# Wyświetlamy nazwy województw i liczbę samochodów
for letter, name in provinces.items():
    print(f'{name}: {vehicle_count[letter]}')

# program to record voting========================================================================================================================================================

import json

file_name = 'voting.json'

# Próbujemy odczytać poprzednie wyniki głosowania
try:
    with open(file_name, 'r', encoding='utf-8') as file:
        voting = json.load(file)

# Jeżeli plik jeszcze nie istnieje, tworzymy pusty słownik
except FileNotFoundError:
    voting = {}

person_name = input('Name of the person you are voting for: ')

# Zwiększamy liczbę głosów istniejącej osoby
if person_name in voting:
    voting[person_name] += 1

# Dodajemy nową osobę
else:
    voting[person_name] = 1

# Zapisujemy aktualne wyniki głosowania
with open(file_name, 'w', encoding='utf-8') as file:
    json.dump(voting, file, indent=4, ensure_ascii=False)

print('Vote saved successfully.')

# program to reverse any text entered from the keyboard========================================================================================================================================================

import queue


def reverse_text(text):

    stack = queue.LifoQueue()

    # Dodajemy wszystkie znaki do stosu
    for char in text:
        stack.put(char)

    reversed_text = ''

    # Pobieramy znaki w odwrotnej kolejności
    while not stack.empty():
        reversed_text += stack.get()

    return reversed_text


text = input('Enter text: ')

print('Reversed text:', reverse_text(text))

# program that calculates RPN expressions========================================================================================================================================================

import queue

stack = queue.LifoQueue()

while True:
    value = input('Enter a number, operator or =: ')

    # Wyświetlamy końcowy wynik
    if value == '=':

        if stack.qsize() == 1:
            print('Result:', stack.get())
            break
        else:
            print('Invalid expression.')
            break

    # Sprawdzamy, czy wprowadzono operator
    elif value in ['+', '-', '*', '/']:

        # Operator wymaga dwóch liczb
        if stack.qsize() < 2:
            print('Not enough numbers.')
            continue

        # Pobieramy dwie liczby ze stosu
        b = stack.get()
        a = stack.get()

        if value == '+':
            result = a + b

        elif value == '-':
            result = a - b

        elif value == '*':
            result = a * b

        elif value == '/':

            if b == 0:
                print('Cannot divide by zero.')
                stack.put(a)
                stack.put(b)
                continue

            result = a / b

        # Dodajemy wynik działania do stosu
        stack.put(result)

    else:

        # Próbujemy zamienić wprowadzoną wartość na liczbę
        try:
            stack.put(float(value))

        except ValueError:
            print('Invalid input.')

# program that supports customer service in an office========================================================================================================================================================

import queue

# Tworzymy kolejkę klientów
customers = queue.Queue()

ticket_number = 1

while True:
    print('\n1. Add customer')
    print('2. Serve customer')
    print('0. Quit')

    menu = input('Select an option: ')

    if menu == '1':

        # Dodajemy numer biletu do kolejki
        customers.put(ticket_number)

        print('Your ticket number:', ticket_number)

        # Zwiększamy numer następnego biletu
        ticket_number += 1

    elif menu == '2':

        # Sprawdzamy, czy są oczekujący klienci
        if not customers.empty():

            # Pobieramy pierwszego klienta
            customer = customers.get()

            print(f'Customer number {customer}, please come forward.')

        else:
            print('No customers in the queue.')

    elif menu == '0':
        break

    else:
        print('Invalid option.')

# program that prints information about a computer========================================================================================================================================================

import json

# Otwieramy plik JSON w trybie odczytu
with open('computer.json', 'r', encoding='utf-8') as file:

    # Odczytujemy dane i zapisujemy je jako słownik
    data = json.load(file)

# Wyświetlamy wszystkie klucze i wartości
for key, value in data.items():
    print(key, ':', value)

# program that prints information about cities========================================================================================================================================================

import json

# Otwieramy plik JSON w trybie odczytu
with open('cities.json', 'r', encoding='utf-8') as file:

    # Odczytujemy listę słowników
    data = json.load(file)

# Przechodzimy przez wszystkie miasta
for city in data:

    # Wyświetlamy wszystkie informacje o mieście
    for key, value in city.items():
        print(key, ':', value)

    # Oddzielamy miasta pustą linią
    print()

# program that prints information about dogs younger than 5 years========================================================================================================================================================

import json

# Odczytujemy dane z pliku JSON
with open('dogs.json', 'r', encoding='utf-8') as file:
    dogs = json.load(file)

# Przechodzimy przez wszystkie psy
for dog in dogs:

    # Sprawdzamy, czy pies ma mniej niż 5 lat
    if dog['age'] < 5:

        # Wyświetlamy wszystkie informacje o psie
        for key, value in dog.items():
            print(f'{key}: {value}')

        # Oddzielamy psy pustą linią
        print()

# program that prints the summary information========================================================================================================================================================

import json


# Funkcja odczytująca rezerwacje z pliku JSON
def read_reservations(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)

    return data['reservations']


# Funkcja obliczająca liczbę rezerwacji
def count_reservations(reservations, paid):
    counter = 0

    for reservation in reservations:
        if reservation['paid'] == paid:
            counter += 1

    return counter


# Funkcja obliczająca całkowitą wartość rezerwacji
def total_value(reservations, paid):
    total = 0

    for reservation in reservations:
        if reservation['paid'] == paid:
            total += reservation['nights'] * reservation['price_per_night']

    return total


# Odczytujemy rezerwacje
reservations = read_reservations('reservations.json')

# Wyświetlamy wyniki
print('Number of rooms:', len(reservations))

print('Number of paid reservations:',
      count_reservations(reservations, True))

print('Number of unpaid reservations:',
      count_reservations(reservations, False))

print(f'Total value of paid reservations: {total_value(reservations, True):.2f}')

print(f'Total value of unpaid reservations: {total_value(reservations, False):.2f}')

# program writes data to a json file========================================================================================================================================================

import json

data = {
    'patient_record': {
        'patient_id': 'P001234',
        'first_name': 'John',
        'last_name': 'Doe',
        'date_of_birth': '1985-05-15',
        'gender': 'Male',
        'contact_info': {
            'phone_number': '+1-555-123-4567',
            'email': 'johndoe@example.com',
            'address': {
                'street': '123 Main St',
                'city': 'New York',
                'state': 'NY',
                'postal_code': '10001',
                'country': 'USA'
            }
        },
        'medical_history': {
            'allergies': ['Penicillin', 'Peanuts'],
            'current_medications': [
                'Lisinopril 10mg',
                'Metformin 500mg'
            ],
            'past_illnesses': [
                'Hypertension',
                'Type 2 Diabetes'
            ],
            'surgeries': [
                {
                    'surgery_type': 'Appendectomy',
                    'date': '2015-08-20'
                }
            ]
        }
    }
}

file_name = 'patient.json'

# Zapisujemy słownik do pliku JSON
with open(file_name, 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4)

print('Data has been written to', file_name)

# program that writes the dictionary data to the favourite.json file========================================================================================================================================================

import json

# Tworzymy słownik opisujący film
movie = {
    'title': 'Inception',
    'director': 'Christopher Nolan',
    'year': 2010,
    'genre': 'Science Fiction',
    'rating': 9.0,
    'duration': 148
}

# Zapisujemy dane do pliku JSON
with open('favourite.json', 'w', encoding='utf-8') as file:
    json.dump(movie, file, indent=4)

print('Movie data saved successfully.')

# program that takes data from the keyboard about a purchased product========================================================================================================================================================

import json

product = {}

# Pobieramy nazwę produktu jako string
product['name'] = input('Enter product name: ')

# Pobieramy cenę jako float
product['price'] = round(float(input('Enter product price: ')), 2)

# Pobieramy informację o płatności
paid = input('Is the product paid? (yes/no): ').lower()

# Sprawdzamy poprawność odpowiedzi
while paid not in ['yes', 'no']:
    paid = input('Enter yes or no: ').lower()

# Zapisujemy informację jako bool
product['paid'] = paid == 'yes'

# Zapisujemy produkt do pliku JSON
with open('product.json', 'w', encoding='utf-8') as file:
    json.dump(product, file, indent=4)

print('Product saved successfully.')

# program that displays the data from the euro.json========================================================================================================================================================

import json

# Odczytujemy dane z pliku JSON
with open('euro.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Wyświetlamy nagłówki tabeli
print(f'{"Date":<16}{"Buying Rate":<16}{"Selling Rate"}')
print('=' * 44)

# Przechodzimy przez wszystkie kursy euro
for rate in data['rates']:

    # Pobieramy datę oraz kursy kupna i sprzedaży
    date = rate['effectiveDate']
    buying_rate = rate['bid']
    selling_rate = rate['ask']

    # Wyświetlamy dane z dokładnością do 4 miejsc po przecinku
    print(f'{date:<16}{buying_rate:<16.4f}{selling_rate:.4f}')