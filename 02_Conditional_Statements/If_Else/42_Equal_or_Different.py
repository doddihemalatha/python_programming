"""
Program: Equal or Different Number Checker
Author: Hema
Concepts Used: Variables, Input, Type Casting, Comparison Operator (==),
if-else, Output
Description: Accepts two numbers from the user and checks whether
both numbers are equal or different.
"""

# LOGIC
# Accept two numbers from the user.
# Compare both numbers using the == operator.
# If both numbers are equal, display "Both numbers are equal".
# Otherwise, display "Both numbers are different".

# CODE
num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

if num1 == num2:
    print("Both numbers are equal")
else:
    print("Both numbers are different")
