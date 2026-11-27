# program that manages a queue of files to print========================================================================================================================================================

import queue

# Tworzymy kolejkę plików do wydrukowania
files_to_print = queue.Queue()

while True:
    print('\n1. Add file to print')
    print('2. Print file')
    print('0. Quit')

    menu = input('Select an option: ')

    if menu == '1':
        file_name = input('Enter file name to print: ')

        # Dodajemy plik na koniec kolejki
        files_to_print.put(file_name)

    elif menu == '2':

        # Sprawdzamy, czy kolejka nie jest pusta
        if not files_to_print.empty():

            # Pobieramy pierwszy plik z kolejki
            file_to_print = files_to_print.get()

            print(f'File {file_to_print} is currently being printed. Please wait!')

        else:
            print('Print queue is empty.')

    elif menu == '0':
        break

    else:
        print('Invalid option.')