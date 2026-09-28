"""
Program: Positive, Negative, or Zero Checker
Author: Hema
Concepts Used: Variables, Input, Type Casting, if-elif-else,
Comparison Operators (>, <), Output
Description: Accepts a number from the user and checks whether
the number is positive, negative, or zero.
"""

# LOGIC
# Accept a number from the user.
# If the number is greater than 0, it is positive.
# If the number is less than 0, it is negative.
# Otherwise, the number is zero.

# CODE
num = float(input("Enter a Number: "))

if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")
