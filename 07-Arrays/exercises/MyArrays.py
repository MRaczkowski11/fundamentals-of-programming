# Sortowanie bez funkcji sorted()
def sort_numbers(arr):
    numbers = arr.copy()

    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers


# Druga największa różna wartość
def second_largest(arr):
    numbers = sort_numbers(arr)
    largest = numbers[-1]

    for i in range(len(numbers) - 2, -1, -1):
        if numbers[i] != largest:
            return numbers[i]

    return None


# Różnica największej i najmniejszej wartości
def difference(arr):
    numbers = sort_numbers(arr)
    return numbers[-1] - numbers[0]


# Mediana uporządkowanych liczb
def median(arr):
    numbers = sort_numbers(arr)
    n = len(numbers)

    if n % 2 == 1:
        return numbers[n // 2]

    return (numbers[n // 2 - 1] + numbers[n // 2]) / 2


# Najmniejsza i największa liczba
def min_max(arr):
    numbers = sort_numbers(arr)
    return [numbers[0], numbers[-1]]


# Liczby oddzielone myślnikami
def numbers_to_string(arr):
    result = ''

    for i in range(len(arr)):
        if i > 0:
            result += '-'
        result += str(arr[i])

    return result
