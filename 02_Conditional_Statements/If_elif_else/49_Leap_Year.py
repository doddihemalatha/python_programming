"""
Program: Leap Year Checker
Author: Hema
Concepts Used: Variables, Input, Type Casting, if-elif-else,
Modulus Operator (%), Comparison Operators (==, !=),
Logical Operator (and), Output
Description: Accepts a year and checks whether it is a leap year
using the standard leap year rules.
"""

# LOGIC
# Accept a year from the user.
# A year is a leap year if:
# 1. It is divisible by 400, OR
# 2. It is divisible by 4 but NOT divisible by 100.
# Otherwise, it is not a leap year.

# CODE
year = int(input("Enter Year: "))

if year % 400 == 0:
    print("Leap Year")

elif year % 4 == 0 and year % 100 != 0:
    print("Leap Year")

else:
    print("Not a Leap Year")
