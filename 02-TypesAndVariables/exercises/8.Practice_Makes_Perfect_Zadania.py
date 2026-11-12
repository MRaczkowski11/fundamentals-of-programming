# Program obliczający obwód i pole koła========================================================================================================================================================================================================

r = float(input('Enter circle radius: '))                        # Pobieranie promienia koła od użytkownika i konwersja na typ float
pi = 3.14

area = pi * r ** 2                     # Obliczanie pola koła za pomocą wzoru π * r², gdzie r to promień koła, a π to stała matematyczna pi (przybliżona wartość 3.14)

circumference = 2 * pi * r                # Obliczanie obwodu koła za pomocą wzoru 2 * π * r, gdzie r to promień koła, a π to stała matematyczna pi (przybliżona wartość 3.14)

print(f'Circle circumference: {circumference:.2f}')
print(f'Circle area: {area:.2f}')

# Program konwertujący temperaturę z Celsjusza na Kelwiny i Fahrenheita========================================================================================================================================================================================================

celsius = float(input('Enter temperature in Celsius: '))                     # Pobieranie temperatury w stopniach Celsjusza od użytkownika i konwersja na typ float

kelvin = celsius + 273.15                        # Obliczanie temperatury w Kelwinach poprzez dodanie 273.15 do temperatury w stopniach Celsjusza

fahrenheit = (celsius * 9/5) + 32                # Obliczanie temperatury w stopniach Fahrenheita za pomocą wzoru (C * 9/5) + 32, gdzie C to temperatura w stopniach Celsjusza

print(f'Temperature in Kelvin: {kelvin:.2f} K')
print(f'Temperature in Fahrenheit: {fahrenheit:.2f} °F')

# Program który wyświetla kod SWIFT banku i kraju na podstawie podanego kodu SWIFT========================================================================================================================================================================================================

swift = input('Enter SWIFT code: ')

bank_code = swift[0:4]
country_code = swift[4:6]

print(f'Bank Code: {bank_code}')
print(f'Country Code: {country_code}')

#BPKOPLPW: Bank Code: BPKO, Country Code: PL
#CHASUS33: Bank Code: CHAS, Country Code: US
#DEUTDEFF: Bank Code: DEUT, Country Code: DE

# Program obliczający koszt transportu na podstawie dystansu, ceny paliwa i zużycia paliwa========================================================================================================================================================================================================

distance = int(input('Enter distance in km: '))
fuel_price = float(input('Enter fuel price per liter: '))
fuel_consumption = float(input('Enter fuel consumption per 100 km: '))

total_fuel_consumption = distance / 100 * fuel_consumption                # Obliczanie całkowitego zużycia paliwa na podstawie podanego dystansu w kilometrach, ceny paliwa za litr i zużycia paliwa na 100 km (total_fuel_consumption = (distance / 100) * fuel_consumption)
total_cost = total_fuel_consumption * fuel_price                        # Obliczanie całkowitego kosztu transportu na podstawie całkowitego zużycia paliwa i ceny paliwa za litr (total_cost = total_fuel_consumption * fuel_price)

print(f'Total fuel consumption: {total_fuel_consumption:.2f} liters')
print(f'Total transportation cost: {total_cost:.2f}')

# Program konwertujący liczbę całkowitą na system binarny i szesnastkowy========================================================================================================================================================================================================

number = int(input('Enter number: '))

binary_number = bin(number)
hexadecimal_number = hex(number)

print(f'Binary number: {binary_number}')
print(f'Hexadecimal number: {hexadecimal_number}')
