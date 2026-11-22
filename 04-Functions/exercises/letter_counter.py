# Function that counts how many times a letter appears in text

def count_letter(text, letter):                                # Defining a function
    counter = 0                                                # Initializing the counter

    for char in text:                                          # Going through each character
        if char == letter:                                     # Checking if the character matches
            counter = counter + 1                              # Increasing the counter

    return counter                                             # Returning the number of occurrences
