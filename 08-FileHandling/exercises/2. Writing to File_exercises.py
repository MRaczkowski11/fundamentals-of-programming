# writes a list of the Seven Wonders of the World to a text file, in alphabetical order, with each name on a separate line========================================================================================================================================================

seven_wonders = [
    'Great Wall of China',
    'Petra',
    'Christ the Redeemer',
    'Machu Picchu',
    'Chichen Itza',
    'Roman Colosseum',
    'Taj Mahal'
]

file_name = 'seven_wonders.txt'

# Sortujemy listę alfabetycznie
seven_wonders = sorted(seven_wonders)

# Zapisujemy każdy element w osobnej linii
with open(file_name, 'w') as file:
    for item in seven_wonders:
        file.write(item + '\n')

print('File created successfully.')

# program that copies the contents of the file 'healthy_lifestyle.txt'========================================================================================================================================================

original_file = 'healthy_lifestyle.txt'
target_file = 'copy_healthy_lifestyle.txt'

# Odczytujemy zawartość oryginalnego pliku
with open(original_file, 'r') as file:
    content = file.read()

# Zapisujemy zawartość do nowego pliku
with open(target_file, 'w') as file:
    file.write(content)

print('File copied successfully.')

# program that saves data of employees employed in the position of 'Software Engineer'========================================================================================================================================================

employees_file = 'it_company.csv'
position_file = 'software_engineer.txt'

job_title = 'Software Engineer'

# Otwieramy plik z pracownikami
with open(employees_file, 'r') as source:

    # Otwieramy plik do zapisu wyników
    with open(position_file, 'w') as target:

        for line in source:

            # Zapisujemy tylko wybranych pracowników
            if job_title in line:
                target.write(line)

print('Employees saved successfully.')

# program that allows you to create a shopping list========================================================================================================================================================

shopping_list = 'shopping_list.txt'


def add_product(file_name, product_name):

    # Dodajemy produkt na końcu istniejącego pliku
    with open(file_name, 'a') as file:
        file.write(product_name + '\n')


product = ''

while product != '0':
    product = input('Enter product name (0 stops): ')

    # Kończymy pętlę po wpisaniu 0
    if product == '0':
        break
    else:
        add_product(shopping_list, product)

print('Shopping list saved.')

