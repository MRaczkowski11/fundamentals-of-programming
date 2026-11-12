# Program do wprowadzania danych ========================================================================================================================================================================================================

first_name = input('Enter your first name: ')                   # Pobieranie imienia od użytkownika
last_name = input('Enter your last name: ')                     # Pobieranie nazwiska od użytkownika

full_name = first_name + ' ' + last_name

print(f'Your first name is {first_name} and your last name is {last_name}')                         
print(f'And your full name is {full_name}')

# Program obliczający objętość i powierzchnię sześcianu ========================================================================================================================================================================================================

cube_side_string = input('Enter cube side: ')                    # Pobieranie długości boku sześcianu od użytkownika
cube_side = int(cube_side_string)

cube_volume = cube_side ** 3
cube_surface_area = 6 * cube_side ** 2

print(f'The volume of a cube with side {cube_side} is {cube_volume}')
print(f'The surface area of a cube with side {cube_side} is {cube_surface_area}')

# Program obliczający objętość i powierzchnię sześcianu 2 ========================================================================================================================================================================================================

a = int(input('a='))
b = int(input('b='))
c = int(input('c='))

volume = a * b * c
surface_area = 2 * (a * b + a * c + b * c)

print(f'The volume of a cuboid is {volume}')
print(f'The surface area of a cuboid is {surface_area}')

# Dla a = 3, b = 4, c = 5
# Objętość prostopadłościanu wynosi 60
# Powierzchnia prostopadłościanu wynosi 94

# Dla a = 8, b =1, c = 2
# Objętość prostopadłościanu wynosi 16
# Powierzchnia prostopadłościanu wynosi 52

# Kalkulator VAT========================================================================================================================================================================================================

amount = float(input('Enter amount: '))               # Pobieranie kwoty od użytkownika i konwersja na typ float

vat = amount * 0.23                        # Obliczanie wartości VAT (23% z kwoty) poprzez pomnożenie kwoty przez 0.23

print(f'Amount  : {amount:.2f}')
print(f'VAT 23% : {vat:5.2f}')

# Kalkulator Przeceny========================================================================================================================================================================================================

price = float(input('Enter price: '))
discount = float(input('Enter discount %: '))

price_with_discount = price - (price * discount / 100)
reduction = price - price_with_discount

print(f'Price with discount: {price_with_discount:.2f}')
print(f'Reduction: {reduction:.2f}')

# Dla price = 24.72, discount = 15
# Price with discount: 21.01
# Reduction: 3.71
