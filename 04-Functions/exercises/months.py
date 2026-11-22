# Function that returns the name of a month based on its number

def month(n):                                                  # Defining a function
    result = ''                                                # Initializing the result

    if n == 1:
        result = 'January'
    elif n == 2:
        result = 'February'
    elif n == 3:
        result = 'March'
    elif n == 4:
        result = 'April'
    elif n == 5:
        result = 'May'
    elif n == 6:
        result = 'June'
    elif n == 7:
        result = 'July'
    elif n == 8:
        result = 'August'
    elif n == 9:
        result = 'September'
    elif n == 10:
        result = 'October'
    elif n == 11:
        result = 'November'
    elif n == 12:
        result = 'December'

    return result                                              # Returning the month name
