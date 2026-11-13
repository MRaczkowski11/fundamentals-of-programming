# Interactive Mode and Script Mode========================================================================================================================================================================================================
#Interactive Mode:

#>>> 7+4
#11

#>>> (30+10) / 2
#20.0

#>>> 2 ** 3
#8

#>>> 7 > 5
#True

#>>> r = 4
#>>> area = 3.14159 * r * r
#>>> area
#50.26544
#>>> round(area,2)                          #Zaokrąglanie liczby do 2 miejsc po przecinku z użyciem funkcji round()
#50.27

#>>> first_name = "Mary"
#>>> last_name = "Brown"
#>>> full_name = first_name + ' ' + last_name            #Łączenie dwóch stringów w jeden z użyciem operatora + i dodanie spacji między nimi
#>>> full_name
#'Mary Brown'
#>>> print(full_name)
#Mary Brown
#>>> len(full_name)                  #Obliczanie długości stringa z użyciem funkcji len()
#10

#>>> a = 5
#>>> h = 4
#>>> triangle_area = (a * h) / 2     #Obliczanie pola trójkąta wzorem (a * h) / 2
#>>> print(triangle_area)
#10.0

#>>> mean = (7 + 12 + 31) / 3              #Obliczanie średniej arytmetycznej trzech liczb wzorem (a + b + c) / 3
#>>> print(round(mean, 2))                   #Zaokrąglanie wyniku do 2 miejsc po przecinku
#16.67

# Script Mode========================================================================================================================================================================================================

# Kod w pliku: 
# Hello = "Hello World!"
# print(Hello)

#PS C:\Users\raczk\Documents> py program_script_mode.py
#Hello World!
#PS C:\Users\raczk\Documents>

# BMI Calculator========================================================================================================================================================================================================

height = input('Podaj wzrost w cm: ')                     # Pobieranie wzrostu od użytkownika
weight = input('Podaj wagę w kg: ')                       # Pobieranie wagi od użytkownika

height = int(height)                           # Konwersja wzrostu na typ int
weight = int(weight)                           # Konwersja wagi na typ int

bmi = weight / (height / 100) ** 2                     # Obliczanie BMI wzorem wagi podzielonej przez kwadrat wzrostu w metrach
bmi = round(bmi, 2)                                    # Zaokrąglanie wyniku BMI do 2 miejsc po przecinku

print('Twoje BMI wynosi:', bmi)
print('Sprawdź w Internecie, czy Twoje BMI jest prawidłowe!')

# Dice Rolling Game========================================================================================================================================================================================================

# Program symuluje pięć rzutów kostką

import random                         # Importowanie modułu random, który umożliwia generowanie losowych liczb

print("Symulator rzucania kostką")

for i in range(5):                            # Pętla for, która wykonuje się 5 razy, aby zasymulować pięć rzutów kostką
    dice_roll = random.randint(1, 6)             # Generowanie losowej liczby całkowitej z zakresu od 1 do 6, która reprezentuje wynik rzutu kostką
    print(dice_roll, end=" ")