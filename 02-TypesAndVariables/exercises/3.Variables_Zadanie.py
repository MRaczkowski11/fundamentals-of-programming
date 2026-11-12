# Variables========================================================================================================================================================================================================

company = "ABC Data"             # Wartość: ABC Data | Typ: str
phone = "555-123-009"            # Wartość: 555-123-009 | Typ: str
employees = 25                   # Wartość: 25 | Typ: int
remote_work = True               # Wartość: True | Typ: bool
big_company = employees > 100    # Wartość: False | Typ: bool
income = 4500000                 # Wartość: 4500000 | Typ: int
income_per_person = income / employees  # Wartość: 180000.0 | Typ: float

# Łącznie jest 7 zmiennych, z czego 3 są typu str, 2 typu int, a 2 typu bool

# Program do obliczania 3 liczb========================================================================================================================================================================================================

number1 = 71
number2 = 14
number3 = 25

result = number1 + number2 + number3          #Obliczanie sumy trzech liczb i przypisanie wyniku do zmiennej result

print('Number 1: ', number1)                  #Wyświetlanie wartości zmiennej number1
print('Number 2: ', number2)                  #Wyświetlanie wartości zmiennej number2
print('Number 3: ', number3)                  #Wyświetlanie wartości zmiennej number3
print('The result of summation: ', result)     #Wyświetlanie wartości zmiennej result

# Program który zamienia wartości 2 zmiennych========================================================================================================================================================================================================

x = 7
y = 34
z = 0                     #Przypisanie wartości 0 do zmiennej z, która będzie używana jako tymczasowa zmienna do przechowywania wartości jednej z dwóch zmiennych podczas zamiany

print("Before swapping: x=", x, "y=", y)

z = x
x = y
y = z

print("After swapping: x=", x, "y=", y)

# Program który zamienia km/h na m/s========================================================================================================================================================================================================

speed_kmh = 70
speed_ms = speed_kmh / 3.6      #Obliczanie prędkości w m/s poprzez podzielenie prędkości w km/h przez 3.6 (ponieważ 1 km/h = 1/3.6 m/s)

print(speed_kmh, "km/h = ", speed_ms, "m/s")                      #Wyświetlanie wyniku konwersji prędkości z km/h na m/s

# program który oblicza przekątną prostokąta========================================================================================================================================================================================================

import math                  #Importowanie modułu math, który zawiera funkcje matematyczne, w tym funkcję sqrt() do obliczania pierwiastka kwadratowego

a = 5
b = 8

diagonal = math.sqrt(a**2 + b**2)              #Obliczanie długości przekątnej prostokąta za pomocą wzoru d = √(a² + b²), gdzie a i b to długości boków prostokąta, a d to długość przekątnej

print("The diagonal length is:", diagonal)

# Program który oblicza dystans do horyzontu========================================================================================================================================================================================================

import math

height = float(input("Enter your height in meters: "))                     #Pobieranie wzrostu od użytkownika w metrach i konwersja na typ float
distance = 3.57 * math.sqrt(height)                                        #Obliczanie dystansu do horyzontu za pomocą wzoru d = 3.57 * √h, gdzie h to wysokość obserwatora w metrach, a d to odległość do horyzontu w kilometrach

print("Distance to the horizon from the beach:", round(distance, 2), "km") 

height = 20
distance = 3.57 * math.sqrt(height)                                                #Obliczanie dystansu do horyzontu z wysokości 20 metrów (np. z hotelu) za pomocą wzoru d = 3.57 * √h, gdzie h to wysokość obserwatora w metrach, a d to odległość do horyzontu w kilometrach

print("Distance to the horizon from the hotel:", round(distance, 2), "km")

# Jeżeli mam 1.80m wzrostu to plaża jest w odległości 4.79 km, a hotel w odległości 15.96 km od horyzontu.

# Program który oblicza ilość i procent osób w północnej i południowej półkuli========================================================================================================================================================================================================

total = 8000000000
north = 7200000000
south = total - north                   #Obliczanie liczby osób w południowej półkuli poprzez odjęcie liczby osób w północnej półkuli od całkowitej liczby osób na świecie

print("World population: ", total)

print("Northern Hemisphere: ", north)
print("Northern Hemisphere in %: ", north / total * 100)                 #Obliczanie procentu osób w północnej półkuli poprzez podzielenie liczby osób w północnej półkuli przez całkowitą liczbę osób na świecie i pomnożenie wyniku przez 100

print("Southern Hemisphere: ", south)
print("Southern Hemisphere in %: ", south / total * 100)              #Obliczanie procentu osób w południowej półkuli poprzez podzielenie liczby osób w południowej półkuli przez całkowitą liczbę osób na świecie i pomnożenie wyniku przez 100

# Program który oblicza średnią ocenę z 4 przedmiotów========================================================================================================================================================================================================

math = 5
art = 4
music = 5
history = 3

average = (math + art + music + history) / 4

print("Average grade is", average)