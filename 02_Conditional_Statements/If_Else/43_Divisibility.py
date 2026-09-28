"""
Program: Divisibility by 5 Checker
Author: Hema
Concepts Used: Variables, Input, Type Casting, Modulus Operator (%),
Comparison Operator (==), if-else, Output
Description: Accepts a number from the user and checks whether the
number is exactly divisible by 5.
"""

# LOGIC
# Accept a number from the user.
# Divide the number by 5 using the modulus operator.
# If the remainder is 0, the number is divisible by 5.
# Otherwise, the number is not divisible by 5.

# CODE
num = int(input("Enter a number: "))

if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not Divisible by 5")
