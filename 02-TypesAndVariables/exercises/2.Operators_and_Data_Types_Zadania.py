# Typy Operatorów========================================================================================================================================================================================================

# +  Dodawanie dwóch liczb
# *  Mnożenie dwóch liczb
# ** Potęgowanie (podnoszenie liczby do potęgi)
# /  Dzielenie dwóch liczb
# // Dzielenie całkowite (bez części ułamkowej)
# %  Reszta z dzielenia (modulo)
# >  Sprawdzenie, czy lewa liczba jest większa od prawej
# <= Sprawdzenie, czy lewa liczba jest mniejsza lub równa prawej

# Number of operators and arguments========================================================================================================================================================================================================

# 1. Wyrażenie: 3 * 2 + 1
# Operatory: 2 (*, +)
# Argumenty: 3 (3, 2, 1)
# Wynik: 7

# 2. Wyrażenie: 5 + 10 * 5
# Operatory: 2 (+, *)
# Argumenty: 3 (5, 10, 5)
# Wynik: 55

# 3. Wyrażenie: 4 + 4 / 2 ** 2
# Operatory: 3 (+, /, **)
# Argumenty: 4 (4, 4, 2, 2)
# Wynik: 5.0

# 4. Wyrażenie: 4 % 3 % 2 % 1
# Operatory: 3 (%)
# Argumenty: 4 (4, 3, 2, 1)
# Wynik: 0

# 5. Wyrażenie: 1 + 2 % 3 ** 4 * 5
# Operatory: 4 (+, %, **, *)
# Argumenty: 5 (1, 2, 3, 4, 5)
# Wynik: 11

# 6. Wyrażenie: True != False
# Operatory: 1 (!=)
# Argumenty: 2 (True, False)
# Wynik: True

# Data Types========================================================================================================================================================================================================

# 1. 50
print(type(50))  # int

# 2. 149.17
print(type(149.17))  # float

# 3. 4 * 7
print(type(4 * 7))  # int

# 4. 4.0 * 7
print(type(4.0 * 7))  # float

# 5. "Krakow University of Economics"
print(type("Krakow University of Economics"))  # str

# 6. True
print(type(True))  # bool

# 7. 2 > 5
print(type(2 > 5))  # bool (False)