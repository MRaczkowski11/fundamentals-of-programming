# 1. Even numbers with while loop======================================================================================================================================================================

arr = [34, 7, 19, 4, 21, 8]

i = 0
counter = 0

while i < len(arr):
    if arr[i] % 2 == 0:
        counter += 1
    i += 1

print('Number of even values:', counter)

# 2. Array in reverse order======================================================================================================================================================================

arr = [15, 8, 31, 47, 2, 19]

print('Existing array:', *arr)

print('Reverse array:', end=' ')

# Przechodzimy od ostatniego indeksu do pierwszego
for i in range(len(arr) - 1, -1, -1):
    print(arr[i], end=' ')

# 3. Second power of each array element======================================================================================================================================================================

arr = [8, 2, 5, 1, 9]

print('Array:', *arr)
print('2nd power:', end=' ')

for number in arr:
    print(number ** 2, end=' ')

# 4. Maximum and minimum number======================================================================================================================================================================

arr = [-15, 8, -31, 47, -2, 19]

minimum = arr[0]
maximum = arr[0]

# Porównujemy każdą liczbę z aktualnym minimum i maksimum
for number in arr:
    if number < minimum:
        minimum = number

    if number > maximum:
        maximum = number

print('Minimum:', minimum)
print('Maximum:', maximum)

# 5. Calculates and prints the array and the arithmetic mean of array values with for loop======================================================================================================================================================================

arr = [15, 8, 31, 47, 2, 19]

total = 0

for number in arr:
    total += number

average = total / len(arr)

print('Array:', *arr)
print('Average:', average)

# 6. Calculates and prints the array and the arithmetic mean of array values with while loop======================================================================================================================================================================

arr = [15, 8, 31, 47, 2, 19]

total = 0
i = 0

while i < len(arr):
    total += arr[i]
    i += 1

average = total / len(arr)

print('Array:', *arr)
print('Average:', average)

# 7. Longest name======================================================================================================================================================================

names = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']

longest_name = names[0]

# Porównujemy długości kolejnych imion
for name in names:
    if len(name) > len(longest_name):
        longest_name = name

print('Names:', *names)
print('Longest name:', longest_name)

# 8. Stars======================================================================================================================================================================

def star(n):
    # Zwracamy n gwiazdek
    return '*' * n


arr = [2, 6, 4, 9, 7]

for number in arr:
    print(str(number) + ':', star(number))

# 9. Comparing two lists======================================================================================================================================================================

def compare(array1, array2):
    # Sprawdzamy długości
    if len(array1) != len(array2):
        return False

    # Sprawdzamy elementy o tych samych indeksach
    for i in range(len(array1)):
        if array1[i] != array2[i]:
            return False

    return True


pairs = [
    (['water', 'book', 'sky'], ['water', 'book', 'sky']),
    ([True, False], [True, False, True]),
    ([5, 3, 1], [5, 3, 1]),
    ([3, 2, 1], [3, 2])
]

# 10. Elements missing in 2nd list======================================================================================================================================================================

array1 = [4, 36, 12, 28, 9, 44, 5]
array2 = [5, 1, 36]

for number in array1:
    if number not in array2:
        print(number, end=' ')


# 11. Bubble sort 3 lists======================================================================================================================================================================

def bubblesort(array):
    n = len(array)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


arr1 = [5, 2, 8, 1, 4]
arr2 = [10, -3, 7, 0, 2]
arr3 = [9, 6, 3, 8, 1]

print('Sorted array 1:', bubblesort(arr1))
print('Sorted array 2:', bubblesort(arr2))
print('Sorted array 3:', bubblesort(arr3))


# 12. Elements appering only once======================================================================================================================================================================

arr = [2, 3, 2, 5, 8, 1, 9, 8]

print('Array:', *arr)
print('Unique elements:', end=' ')

# Wyświetlamy tylko liczby występujące jeden raz
for number in arr:
    if arr.count(number) == 1:
        print(number, end=' ')


# 13. Checking for presence of numbers======================================================================================================================================================================

def occurs(number, array):
    for item in array:
        if item == number:
            return True
    return False


arr = [15, 38, 7, 23, 14]
number = int(input('Number: '))

print('Array:', *arr)

if occurs(number, arr):
    print('Result: number', number, 'appears in the array')
else:
    print('Result: number', number, 'does not appear in the array')

# 14. Tuple "computation"======================================================================================================================================================================

# Przecinek tworzy krotkę jednoelementową
word = ('computation',)

print('Tuple:', word)
print('Type:', type(word))

# 15. Reverse tuple======================================================================================================================================================================

numbers = (10, 20, 30, 40, 50)

print('Tuple:', numbers)
print('Reverse order:', numbers[::-1])

# 16. Elements of tuple======================================================================================================================================================================

data = ('Seven', [10, 20, 30], (5, 15, 25))

# Pierwszy element krotki
print(data[0])

# Trzeci element listy wewnątrz krotki
print(data[1][2])

# 17. Number of occurrences of any value from a tuple======================================================================================================================================================================

numbers = (50, 20, 40, 50, 30, 50)

value = 50

print('Tuple:', numbers)
print('Value:', value)
print('Number of occurrences:', numbers.count(value))

# 18. module MyArrays containing functions======================================================================================================================================================================

import MyArrays

numbers = [7, 3, 8, 5, 2]

print('Numbers:', numbers)
print('Second largest number:', MyArrays.second_largest(numbers))
print('Difference:', MyArrays.difference(numbers))
print('Median:', MyArrays.median(numbers))
print('Smallest and largest:', MyArrays.min_max(numbers))
print('Numbers as a string:', MyArrays.numbers_to_string(numbers))

# 19. number of elements that are greater than the given value entered from the keyboard======================================================================================================================================================================

arr = [3.5, 7.2, 1.8, 9.4, 5.0, 6.7]

value = float(input('Enter value: '))
counter = 0

# Liczymy elementy większe od podanej liczby
for number in arr:
    if number > value:
        counter += 1

print('Array:', *arr)
print('Number of greater elements:', counter)

# 20. separate even and odd numbers of a given array of integers======================================================================================================================================================================

arr = [7, 9, 2, 4, 5, 6]

even_numbers = []
odd_numbers = []

# Rozdzielamy liczby według parzystości
for number in arr:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

# Łączymy obie listy
arr = even_numbers + odd_numbers

print('Array:', arr)

# 21. checks whether the first array is a subset of the second one======================================================================================================================================================================

array1 = [2, 4, 6]
array2 = [1, 2, 3, 4, 5, 6]

is_subset = True

# Sprawdzamy, czy każdy element pierwszej listy jest w drugiej
for number in array1:
    if number not in array2:
        is_subset = False
        break

print('First array:', array1)
print('Second array:', array2)
print('Is subset:', is_subset)

# 22. returns a randomly selected array element======================================================================================================================================================================

import random

def rand_elem(array):
    # Losujemy indeks elementu
    index = random.randint(0, len(array) - 1)
    return array[index]


numbers = [10, 20, 30, 40, 50]

for i in range(5):
    print('Random element:', rand_elem(numbers))

# 23. call the functions and print results======================================================================================================================================================================

import MyText

text = 'An apple a day keeps the doctor away'

print('Text:', text)
print('Number of words:', MyText.word_count(text))
print('Words from the longest:', ', '.join(MyText.longest_words(text)))
print('Words ordered alphabetically:', ', '.join(MyText.alphabetical_words(text)))

# 24. using ‘matplotlib’, draw a line in a diagram======================================================================================================================================================================


import matplotlib.pyplot as plt

# Współrzędne dwóch punktów
xpoints = [1, 8]
ypoints = [3, 10]

# Rysujemy odcinek
plt.plot(xpoints, ypoints)

# Wyświetlamy wykres
plt.show()

# 25. draws the graph of the function f(x)=x2-3======================================================================================================================================================================

import matplotlib.pyplot as plt

x = []
y = []

# Tworzymy wartości x od -100 do 100
for n in range(-100, 101):
    x.append(n)

# Obliczamy y dla każdej wartości x
for n in x:
    y.append(n ** 2 - 3)

# Rysujemy wykres
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('y = x^2 - 3')
plt.grid(True)
plt.show()

# 26. draws the function y = sin(x) for an angle value in the range 0-360 degrees======================================================================================================================================================================

import math
import matplotlib.pyplot as plt

x = []
y = []

# Obliczamy sinus dla kolejnych kątów
for angle in range(0, 361):
    x.append(angle)
    y.append(math.sin(math.radians(angle)))

plt.plot(x, y)
plt.xlabel('Angle (degrees)')
plt.ylabel('sin(x)')
plt.title('Sine function')
plt.grid(True)
plt.show()

# 27. prints array values in rows and columns======================================================================================================================================================================

arr = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]

# Wyświetlamy elementy w wierszach i kolumnach
for row in arr:
    for number in row:
        print(number, end=' ')
    print()


# 28. calculates the sum of values in the last column======================================================================================================================================================================

arr = [
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
    [8, 7, 1, 1, 5]
]

total = 0

# Pobieramy ostatni element każdego wiersza
for row in arr:
    total += row[-1]

print('Sum of last column:', total)

# 29. two-dimensional array with dimensions of 3 by 5======================================================================================================================================================================

def create_2d_arr(x, y):
    arr = []

    # Tworzymy x wierszy
    for i in range(x):
        row = []

        # Dodajemy y zer do każdego wiersza
        for j in range(y):
            row.append(0)

        arr.append(row)

    return arr


numbers = create_2d_arr(3, 5)

for row in numbers:
    print(*row)

# 30. modifies the array values to create a multiplication table======================================================================================================================================================================

arr = [[0 for j in range(5)] for i in range(5)]

# Wypełniamy tablicę wynikami mnożenia
for i in range(5):
    for j in range(5):
        arr[i][j] = (i + 1) * (j + 1)

# Wyświetlamy tabliczkę mnożenia
for row in arr:
    for number in row:
        print(f'{number:3}', end='')
    print()

# 31. finds the smallest and largest values in the array and in which row and column they are located======================================================================================================================================================================

arr = [
    [-38, 19],
    [5, 40],
    [-7, 11],
    [29, 16]
]

minimum = arr[0][0]
maximum = arr[0][0]

min_row = 0
min_col = 0
max_row = 0
max_col = 0

# Sprawdzamy każdy element tablicy
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] < minimum:
            minimum = arr[i][j]
            min_row = i
            min_col = j

        if arr[i][j] > maximum:
            maximum = arr[i][j]
            max_row = i
            max_col = j

print('Minimum:', minimum)
print('Row:', min_row + 1, 'Column:', min_col + 1)

print('Maximum:', maximum)
print('Row:', max_row + 1, 'Column:', max_col + 1)


# 32. swaps the first and the last row======================================================================================================================================================================

arr = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

print('Before:')
for row in arr:
    print(*row)

# Zamieniamy pierwszy i ostatni wiersz
arr[0], arr[-1] = arr[-1], arr[0]

print('After:')
for row in arr:
    print(*row)


# 33. swaps the first and the last column======================================================================================================================================================================

arr = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

print('Before:')
for row in arr:
    print(*row)

# Zamieniamy pierwszą i ostatnią kolumnę
for row in arr:
    row[0], row[-1] = row[-1], row[0]

print('After:')
for row in arr:
    print(*row)


# 34. prints three identity matrices with dimensions of 3, 5 and 8======================================================================================================================================================================

def identity_matrix(n):
    matrix = []

    for i in range(n):
        row = []

        for j in range(n):
            # Jedynka na głównej przekątnej
            if i == j:
                row.append(1)
            else:
                row.append(0)

        matrix.append(row)

    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(*row)


# Wyświetlamy trzy macierze
for size in [3, 5, 8]:
    print('Identity matrix', size, 'x', size)
    print_matrix(identity_matrix(size))
    print()

# 35. prints transposed matrices, in rows and columns======================================================================================================================================================================

def transpose_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    result = []

    # Zamieniamy wiersze z kolumnami
    for j in range(columns):
        new_row = []

        for i in range(rows):
            new_row.append(matrix[i][j])

        result.append(new_row)

    return result


def print_matrix(matrix):
    for row in matrix:
        print(*row)


matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0]
]

matrix3 = [[5, 6, 7, 8]]

for matrix in [matrix1, matrix2, matrix3]:
    print('Original matrix:')
    print_matrix(matrix)

    print('Transposed matrix:')
    print_matrix(transpose_matrix(matrix))
    print()

# 36. prints 1D array for the following 2D arrays======================================================================================================================================================================

def convert_to_1d(array):
    result = []

    # Przechodzimy przez każdy wiersz
    for row in array:
        # Dodajemy elementy wiersza do jednej listy
        for number in row:
            result.append(number)

    return result


arr1 = [
    [2, 3],
    [1, 5]
]

arr2 = [
    [5, 0, 3, 7, 5],
    [9, 0, 9, 1, 2]
]

arr3 = [
    [2, 1],
    [3, 5],
    [7, 4],
    [2, 6]
]

print('Array 1:', convert_to_1d(arr1))
print('Array 2:', convert_to_1d(arr2))
print('Array 3:', convert_to_1d(arr3))
