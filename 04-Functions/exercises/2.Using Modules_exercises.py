# 1. Program for testing functions from the math module======================================================================================================================================================================

import math                                                   # Importing the math module

square_root = math.sqrt(7)                                    # Calculating the square root of 7
print('A square root of 7 is', square_root)

natural_logarithm = math.log(5)                               # Calculating the natural logarithm of 5
print('The natural logarithm of 5 is', natural_logarithm)

sine = math.sin(math.radians(90))                             # Calculating the sine of 90 degrees
print('The sine of 90 degrees is', sine)


# Program that simulates rolling a dice

import random                                                 # Importing the random module

dice_number = random.randint(1, 6)                            # Generating a random number between 1 and 6

print('The dice rolled:', dice_number)                        # Printing the result