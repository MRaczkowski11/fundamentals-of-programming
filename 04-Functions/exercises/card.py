# Function that hides credit card number digits

def hide(card_number):                                         # Defining a function
    result = card_number[:2]                                   # Keeping the first two digits
    result = result + '*' * 10                                 # Replacing ten digits with asterisks
    result = result + card_number[-4:]                         # Keeping the last four digits

    return result                                              # Returning the hidden card number