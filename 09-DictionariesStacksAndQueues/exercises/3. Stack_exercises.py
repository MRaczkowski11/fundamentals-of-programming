# program in which play with stacks========================================================================================================================================================

import queue

# Tworzymy stos
stack = queue.LifoQueue()

# Dodajemy liczby do stosu
stack.put(2)
stack.put(3)
stack.put(7)
stack.put(4)
stack.put(1)
stack.put(9)
stack.put(8)

# Pobieramy i sumujemy dwa ostatnie elementy
first = stack.get()
second = stack.get()

print('Sum of last two numbers:', first + second)

total = 0

# Sumujemy pozostałe elementy stosu
while not stack.empty():
    total += stack.get()

print('Sum of remaining numbers:', total)

# Back key program========================================================================================================================================================

import queue

# Tworzymy stos odwiedzonych stron
visited_websites = queue.LifoQueue()

# Dodajemy wcześniej odwiedzone strony
visited_websites.put('instagram.com')
visited_websites.put('uek.krakow.pl')
visited_websites.put('microsoft.com')

while True:
    website = input('Enter website name (0 for back): ')

    if website == '0':

        # Kończymy program, jeżeli stos jest pusty
        if visited_websites.empty():
            break
        else:
            print('<-- Going back to a previously visited website')
            website = visited_websites.get()

    elif website != "":

        # Dodajemy nową stronę do stosu
        visited_websites.put(website)

    # Wyświetlamy aktualnie odwiedzaną stronę
    print('You are currently viewing:', website)
    print()

# program that checks the correctness of the expressions========================================================================================================================================================

import queue

expression1 = '[(2+3)*4+5]/6-{(7*8)+[4]}'
expression2 = '[(2+3]/4)'
expression3 = '(2-3*4+(5/6)'


def brackets_ok(expression):

    # Tworzymy stos nawiasów
    stack = queue.LifoQueue()

    # Słownik pasujących nawiasów
    brackets = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in expression:

        # Dodajemy nawias otwierający do stosu
        if char in '([{':
            stack.put(char)

        # Sprawdzamy nawias zamykający
        elif char in ')]}':

            # Brak nawiasu otwierającego
            if stack.empty():
                return False

            opening = stack.get()

            # Sprawdzamy, czy nawiasy do siebie pasują
            if opening != brackets[char]:
                return False

    # Jeżeli stos jest pusty, wszystkie nawiasy zostały zamknięte
    return stack.empty()


if brackets_ok(expression1):
    print('Expression 1: Brackets are correct.')
else:
    print('Expression 1: Brackets are incorrect.')

if brackets_ok(expression2):
    print('Expression 2: Brackets are correct.')
else:
    print('Expression 2: Brackets are incorrect.')

if brackets_ok(expression3):
    print('Expression 3: Brackets are correct.')
else:
    print('Expression 3: Brackets are incorrect.')

# program that converts any natural number to a binary number========================================================================================================================================================

import queue

number = int(input('Natural number: '))

stack = queue.LifoQueue()

# Osobno obsługujemy liczbę 0
if number == 0:
    stack.put(0)

# Dzielimy liczbę przez 2 i zapisujemy reszty
while number > 0:
    remainder = number % 2
    stack.put(remainder)

    number = number // 2

print('Binary number: ', end='')

# Pobieramy reszty w odwrotnej kolejności
while not stack.empty():
    print(stack.get(), end='')

print()