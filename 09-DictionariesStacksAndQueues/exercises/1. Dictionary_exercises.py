# dictionary describing your mobile phone========================================================================================================================================================

mobile = {
    'OS': 'Android',
    'Brand': 'Samsung',
    'Model': 'Galaxy S24',
    'RAM': '8 GB',
    'Storage': '256 GB',
    'Color': 'Black'
}

# Wyświetlamy wszystkie klucze i wartości
for key, value in mobile.items():
    print(f'{key} : {value}')

# program that displays dictinary contents========================================================================================================================================================

person = {
    'name': 'Marek',
    'surname': 'Banach',
    'age': 25,
    'hobby': ['swimming', 'excursions'],
    'married': True,
    'phone': {
        'landline': '123444321',
        'mobile': '777888999'
    }
}

# Wyświetlamy imię
print(person['name'])

# Wyświetlamy zainteresowania
print(person['hobby'])

# Wyświetlamy cały słownik
print(person)

# Zmieniamy nazwisko
person['surname'] = 'Nowak'

# Zmieniamy stan cywilny na przeciwny
person['married'] = not person['married']

# Dodajemy płeć
person['gender'] = 'male'

# Dodajemy nowe zainteresowanie do listy
person['hobby'].append('bicycle')

# Dodajemy numer telefonu służbowego
person['phone']['work'] = '313131444'

# Wyświetlamy zmodyfikowany słownik
for key, value in person.items():
    print(f'{key}: {value}')

# array with 5 dictionaries, each containing a country and its population========================================================================================================================================================

countries = [
    {'name': 'Poland', 'population': 38000000},
    {'name': 'Germany', 'population': 83000000},
    {'name': 'France', 'population': 68000000},
    {'name': 'Japan', 'population': 125000000},
    {'name': 'Canada', 'population': 40000000}
]

print(f'{"COUNTRY":<12} POPULATION')

# Przechodzimy przez wszystkie słowniki na liście
for country in countries:
    print(f'{country["name"]:<12} {country["population"]}')


# program that prints details of people from the phone book========================================================================================================================================================

phone_book = {
    'John': '555-1234',
    'David': '555-5678',
    'Bob': '555-8765',
    'Charlie': '555-4321',
    'Diana': '555-9876',
    'Eve': '555-6543',
    'Frank': '555-3456',
    'Grace': '555-7890',
    'Hank': '555-1111',
    'Ivy': '555-2222',
    'Jack': '555-3333',
    'Daniel': '555-4444',
    'Liam': '555-5555',
    'Mia': '555-6666',
    'Nina': '555-7777',
    'Oscar': '555-8888',
    'Paul': '555-9999',
    'Dominic': '555-1010',
    'Rachel': '555-2020',
    'Sam': '555-3030'
}

# Pobieramy imiona i numery telefonów
for name, phone in phone_book.items():

    # Sprawdzamy, czy imię zaczyna się od D
    if name.startswith('D'):
        print(f'{name}: {phone}')


# program that prints a list of products and the quantity========================================================================================================================================================

products = {
    'Laptop': 15,
    'Desktop PC': 10,
    'Monitor': 25,
    'Keyboard': 50,
    'Mouse': 60,
    'External Hard Drive': 30,
    'Printer': 12,
    'Router': 20,
    'USB Flash Drive': 100,
    'Graphics Card': 8
}

total = 0

# Wyświetlamy produkty i sumujemy ich ilości
for product, quantity in products.items():
    print(f'{product}: {quantity}')
    total += quantity

print('Total number of products:', total)


# program that a price list of items from a clothing store========================================================================================================================================================

price_list = {
    'T-shirt': 19.99,
    'Jeans': 49.99,
    'Jacket': 89.99,
    'Sneakers': 59.99,
    'Hat': 15.99
}

# Wyświetlamy ceny przed obniżką
print('Prices before discount:')

for product, price in price_list.items():
    print(f'{product}: {price:.2f}')

# Obliczamy sumę cen przed obniżką
total_before = sum(price_list.values())

print(f'Total before discount: {total_before:.2f}')

# Obniżamy wszystkie ceny o 10%
for product in price_list:
    price_list[product] = round(price_list[product] * 0.9, 2)

# Wyświetlamy ceny po obniżce
print('\nPrices after discount:')

for product, price in price_list.items():
    print(f'{product}: {price:.2f}')

# Obliczamy sumę cen po obniżce
total_after = sum(price_list.values())

print(f'Total after discount: {total_after:.2f}')


