"""
Program: Print Multiplication Table
Author: Hema
Concepts Used: For Loop, range(), input(), int(), print()
Description: Prints the multiplication table of a given number from 1 to 10.
"""

# LOGIC
# 1. Get a number from the user.
# 2. Use range(1, 11) to generate numbers from 1 to 10.
# 3. Multiply the given number by each number.
# 4. Print each multiplication result.

# CODE
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)
