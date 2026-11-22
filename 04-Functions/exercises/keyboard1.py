# Functions to read any data type from the keyboard

def input_string(message):                                    # Reading a string
    value = input(message)
    return value

def input_integer(message):                                   # Reading an integer
    value = input(message)
    return int(value)

def input_real(message):                                      # Reading a real number
    value = input(message)
    return float(value)

def input_boolean(message):                                   # Reading a boolean value
    value = input(message)
    return value.lower() == 'y'
