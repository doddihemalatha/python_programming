"""
Program: Print Multiplication Table
Author: Hema
Concepts Used: While Loop, Variables, Arithmetic Operators, input(), int(), print()
Description: Prints the multiplication table of a given number from 1 to 12 using a while loop.
"""

# LOGIC
# 1. Get a number from the user.
# 2. Initialize x to 1.
# 3. Check whether x is less than or equal to 12.
# 4. Multiply the given number by x and print the result.
# 5. Increment x by 1 in each iteration.
# 6. Repeat until x becomes greater than 12.

# CODE
num = int(input("Enter Number: "))
x = 1

while x <= 12:
    print(num, "*", x, "=", num * x)
    x = x + 1
