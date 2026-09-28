"""
Program: Even or Odd Number Checker
Author: Hema
Concepts Used: Variables, Input, Type Casting, Modulus Operator (%),
Comparison Operator (==), if-else, Output
Description: Accepts a number from the user and checks whether it
is even or odd using the modulus operator.
"""

# LOGIC
# Accept a number from the user.
# Divide the number by 2 using the modulus operator.
# If the remainder is 0, the number is even.
# Otherwise, the number is odd.

# CODE
num = float(input("Enter a Number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
