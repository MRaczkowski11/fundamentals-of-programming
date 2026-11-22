# 1. Program prints elements from a list======================================================================================================================================================================

arr = [2, 3, 7, 5, 4]

print('Array:', arr)
print('Number of elements:', len(arr))
print('First value:', arr[0])
print('Second value:', arr[1])
print('Last value:', arr[-1])

# Przedostatni element bez indeksu ujemnego
print('Last but one value:', arr[len(arr) - 2])

# Suma pierwszego i ostatniego elementu
print('Sum of first and last:', arr[0] + arr[-1])

# Środkowy element listy
print('Middle value:', arr[len(arr) // 2])

# Wyświetlanie elementów w jednej linii
for number in arr:
    print(number, end=' ')

# 2. Program modifies list======================================================================================================================================================================

arr = [1, 2, 3, 4, 5]

print('Array:', arr)

# Odejmujemy 1 od pierwszego elementu
arr[0] -= 1
print('Array:', arr)

# Zwiększamy ostatni element o 4
arr[-1] += 4
print('Array:', arr)

# Mnożymy środkowy element przez 2
arr[len(arr) // 2] *= 2
print('Array:', arr)

# 3. Names of days in a week======================================================================================================================================================================

def weekday(n):
    weekdays = [
        'Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday', 'Sunday'
    ]

    # Odejmujemy 1, ponieważ indeksy zaczynają się od 0
    return weekdays[n - 1]


print(weekday(1))
print(weekday(4))
print(weekday(7))

# 4. Shopping list======================================================================================================================================================================

shopping_list = [
    'milk', 'bread', 'eggs', 'butter', 'cheese',
    'tomatoes', 'potatoes', 'carrots', 'onions', 'garlic'
]

# Wyświetlamy każdy produkt w osobnej linii
for item in shopping_list:
    print(item)

# 5. Game sorting with while loop======================================================================================================================================================================

computer_games = [
    'Minecraft', 'Fortnite', 'Cyberpunk 2077', 'The Witcher 3',
    'League of Legends', 'Valorant', 'Grand Theft Auto V',
    'Elden Ring', 'Apex Legends', 'Call of Duty: Warzone'
]

# Sortujemy gry alfabetycznie
computer_games = sorted(computer_games)

i = 0

# Wyświetlamy ponumerowaną listę
while i < len(computer_games):
    print(i + 1, computer_games[i])
    i += 1

# 6. registring cars from kraków======================================================================================================================================================================

polish_license_plates = [
    'KR5233F', 'PO6987E', 'KR16179', 'BI7192L', 'KK12255',
    'WA7930T', 'SK6922I', 'KK61108', 'KR90538', 'BI8052Q',
    'KK54985', 'LU4864U'
]

counter = 1

# Sprawdzamy początek każdego numeru rejestracyjnego
for car_number in polish_license_plates:
    if car_number.startswith('KR') or car_number.startswith('KK'):
        print(counter, car_number)
        counter += 1

# 7. Test statystics======================================================================================================================================================================

test_results = [
    False, True, False, True, True,
    True, True, False, True, True,
    False, True, True, True, False
]

# Liczba wszystkich pytań
question_number = len(test_results)

# Liczba poprawnych odpowiedzi
correct_answers = 0

for answer in test_results:
    if answer == True:
        correct_answers += 1

# Liczba niepoprawnych odpowiedzi
incorrect_answers = question_number - correct_answers

# Procent poprawnych odpowiedzi
percentage = correct_answers / question_number * 100

print('TEST STATISTICS')
print('===============')
print('Number of questions:', question_number)
print('Number of correct answers:', correct_answers)
print('Number of incorrect answers:', incorrect_answers)
print(f'Percentage of correct answers: {percentage:.2f}%')

# 8. Temperature report from march======================================================================================================================================================================

temperatures = [
    3, 7, 1, -2, 6, -4, 5, 1, 2, 3,
    4, -1, 0, 2, -1, -2, 5, -2, 7, 2,
    -1, 4, 1, -4, 2, 3, 6, 7, 5, 7
]

# Liczba pomiarów
measurements = len(temperatures)

# Obliczamy średnią temperaturę
temp_total = 0

for temp in temperatures:
    temp_total += temp

avg_temp = temp_total / measurements

# Najniższa i najwyższa temperatura
min_temp = min(temperatures)
max_temp = max(temperatures)

# Liczymy dni z ujemną temperaturą
negative_temp = 0
i = 0

while i < len(temperatures):
    if temperatures[i] < 0:
        negative_temp += 1
    i += 1

print('TEMPERATURE REPORT')
print('Month: March')
print('Number of measurements:', measurements)
print(f'Average temperature: {avg_temp:.2f}')
print('Minimum temperature:', min_temp)
print('Maximum temperature:', max_temp)
print('Days with negative temperature:', negative_temp)

# 9. Most expensive category======================================================================================================================================================================

categories = ['Food', 'Transport', 'Rent', 'Entertainment']
expenses = [500, 150, 1000, 200]

# Znajdujemy największy wydatek
highest_expense = max(expenses)

# Znajdujemy jego indeks
index = expenses.index(highest_expense)

# Odczytujemy kategorię o tym samym indeksie
print('Most expensive category:', categories[index])
print('Amount:', highest_expense)

# 10. Price of products====================================================================================================================================================================== 

product_prices = [
    2999.99, 149.99, 499.99, 89.99, 1199.99,
    349.99, 189.99, 99.99, 249.99, 999.99
]

product_quantities = [5, 20, 10, 15, 7, 12, 25, 18, 9, 4]

total_value = 0

# Mnożymy cenę produktu przez jego ilość
for i in range(len(product_prices)):
    total_value += product_prices[i] * product_quantities[i]

print(f'Total stock value: {total_value:.2f}')

# 11. Bubble sort======================================================================================================================================================================

def bubble_sort(arr):
    n = len(arr)

    # Wykonujemy kolejne przebiegi sortowania
    for i in range(n - 1):
        # Porównujemy sąsiednie elementy
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Zamieniamy elementy miejscami
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
bank_transactions = [-150, -20, 300, -45, -60, 500, -120]

print('Original fuel consumption:', car_fuel_consumption)
print('Sorted fuel consumption:', bubble_sort(car_fuel_consumption))

print('Original bank transactions:', bank_transactions)
print('Sorted bank transactions:', bubble_sort(bank_transactions))

# 12. Built-in function sort======================================================================================================================================================================

distances_traveled = [120, 150, 180, 90, 200, 175, 160]

daily_temperatures = [16, 17, 15, 14, 18, 19, 17, 15, 16, 18]

file_names = [
    'report.docx', 'presentation.pptx', 'data.csv',
    'photo.jpg', 'notes.txt', 'invoice.pdf',
    'resume.docx', 'budget.xlsx', 'meeting.mp4', 'schedule.pdf'
]

# Sortowanie rosnące
print('Distances:', sorted(distances_traveled))

# Sortowanie malejące
print('Temperatures:', sorted(daily_temperatures, reverse=True))

# Sortowanie nazw plików
print('Files:', sorted(file_names))

