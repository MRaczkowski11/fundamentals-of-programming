# Functions for converting length units

def cm_to_m(cm):                                              # Converting centimeters to meters
    return cm / 100

def m_to_cm(m):                                               # Converting meters to centimeters
    return m * 100

def cm_to_inches(cm):                                         # Converting centimeters to inches
    return cm / 2.54

def feet_inches_to_cm(feet, inches):                          # Converting feet and inches to centimeters
    total_inches = feet * 12 + inches                         # Converting feet into inches
    return total_inches * 2.54                                # Converting inches into centimeters