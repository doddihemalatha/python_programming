"""
Program: Height Category Checker
Author: Hema
Concepts Used: Variables, Input, Type Casting, if-else,
Comparison Operator (>=), Output
Description: Accepts a person's height and checks whether the person
is classified as tall or short based on a given height threshold.
"""

# LOGIC
# Accept the person's height.
# Check whether the height is 170 or above.
# If yes, display "Tall".
# Otherwise, display "Short".


# CODE
height = float(input("Enter Your Height: "))

if height >= 170:
    print("Tall")
else:
    print("Short")
