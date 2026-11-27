# 1 . printed list of countries is numbered========================================================================================================================================================

counter = 1

with open('countries.txt', 'r') as file:
    for line in file:

        # Wyświetlamy numer i zawartość linii
        print(f'{counter}. {line}', end='')

        counter += 1

# print a list of countries sorted alphabetically========================================================================================================================================================

def read_from_file(name):
    with open(name, 'r') as file:
        content = file.read()

    return content


# Odczytujemy cały plik
file_content = read_from_file('countries.txt')

# Zamieniamy zawartość pliku na listę linii
file_lines = file_content.splitlines()

# Sortujemy listę alfabetycznie
file_lines = sorted(file_lines)

# Wyświetlamy posortowane kraje
for line in file_lines:
    print(line)

# program to calculate the total number of parked cars========================================================================================================================================================

def read_from_file(name):
    with open(name, 'r') as file:
        content = file.read()

    return content


file_content = read_from_file('car_park.txt')
file_lines = file_content.splitlines()

total = 0

# Zamieniamy każdą linię na liczbę całkowitą
for line in file_lines:
    total += int(line)

print('Total cars parked:', total)

# prints the text and counts the number of words in the text========================================================================================================================================================

total_words = 0

with open('pets.txt', 'r') as file:
    for line in file:

        # Wyświetlamy tekst
        print(line, end='')

        # Dzielimy linię na słowa
        words = line.split()

        # Dodajemy liczbę słów do sumy
        total_words += len(words)

print()
print('Number of words:', total_words)

# displays only employees with the position "Software Engineer"========================================================================================================================================================

file_name = 'it_company.csv'
job_title = 'Software Engineer'

counter = 1

with open(file_name, 'r') as file:
    for line in file:

        # Sprawdzamy, czy linia zawiera nazwę stanowiska
        if job_title in line:
            print(f'{counter}. {line}', end='')
            counter += 1
