# 1. Tic-Tac-Toe======================================================================================================================================================================

tic_tac_toe_board = [
    ['X', 'O', 'X'],
    [' ', 'X', 'O'],
    ['O', ' ', 'X']
]

# Przechodzimy przez kolejne wiersze
for row in tic_tac_toe_board:
    # Wyświetlamy elementy danego wiersza
    for cell in row:
        print(cell, end=' ')
    print()

# 2. Monthly and weekly expenses======================================================================================================================================================================

monthly_expenses = [
    [200, 50, 100],
    [180, 60, 110],
    [220, 55, 105],
    [210, 65, 95]
]

categories = ['Food', 'Transport', 'Utilities']
category_totals = [0, 0, 0]
week_totals = []
month_total = 0

# Sumujemy wydatki w każdej kategorii i tygodniu
for week in monthly_expenses:
    week_total = 0

    for i in range(len(week)):
        category_totals[i] += week[i]
        week_total += week[i]

# 3. Weekly meal plan======================================================================================================================================================================

meal_plan = [
    ['Oatmeal', 'Grilled Chicken Salad', 'Spaghetti'],
    ['Pancakes', 'Sandwich', 'Steak'],
    ['Smoothie', 'Chicken Wrap', 'Salmon'],
    ['Eggs', 'Pasta', 'Soup'],
    ['Toast', 'Burrito', 'Pizza'],
    ['Cereal', 'Salad', 'Fish Tacos'],
    ['Bagel', 'Rice and Beans', 'Stir-fry']
]

def weekday(n):
    weekdays = [
        'Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday', 'Sunday'
    ]
    return weekdays[n - 1]


def day_meal_plan(meal_plan, day_number):
    # Pobieramy posiłki dla wybranego dnia
    meals = meal_plan[day_number - 1]
    return ', '.join(meals)


print('WEEKLY MEAL PLAN')
print('(Breakfast, Lunch, Dinner)')
print('==========================')

for day in range(1, 8):
    print(weekday(day) + ':', day_meal_plan(meal_plan, day))

# 4. Cinema's seating arrangement======================================================================================================================================================================

cinema_seats = [
    ['A', 'A', 'B', 'A', 'A'],
    ['A', 'B', 'B', 'A', 'A'],
    ['A', 'A', 'A', 'A', 'B'],
    ['B', 'A', 'A', 'A', 'A'],
    ['A', 'B', 'A', 'A', 'A']
]

def seats_total(seats):
    total = 0
    for row in seats:
        total += len(row)
    return total


def seats_available(seats):
    available = 0
    for row in seats:
        for seat in row:
            if seat == 'A':
                available += 1
    return available


def seats_booked(seats):
    booked = 0
    for row in seats:
        for seat in row:
            if seat == 'B':
                booked += 1
    return booked


def seat_status(seats, row, place):
    # Numery miejsc zaczynają się od 1, indeksy od 0
    if seats[row - 1][place - 1] == 'A':
        return 'Available'
    return 'Booked'


print('CINEMA INFORMATION TABLE')
print('Total seats:', seats_total(cinema_seats))
print('Seats available:', seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats, 1, 1))
print('Seat in row 5, place 5:', seat_status(cinema_seats, 5, 5))
print('Seat in row 3, place 5:', seat_status(cinema_seats, 3, 5))


# 5. Replaces the values of the main diagonal with 1======================================================================================================================================================================

matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Ustawiamy jedynki na głównej przekątnej
for i in range(len(matrix)):
    matrix[i][i] = 1

# Wyświetlamy macierz
for row in matrix:
    for number in row:
        print(number, end=' ')
    print()
