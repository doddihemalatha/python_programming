"""
Program: Print Multiples of 5 up to N
Author: Hema
Concepts Used: While Loop, if statement, Modulus Operator, Variables, Increment Operator, input(), int(), print()
Description: Prints all multiples of 5 up to N using a while loop.
"""

# LOGIC
# 1. Get the ending number from the user.
# 2. Initialize x to 1.
# 3. Check whether x is less than or equal to N.
# 4. If x is divisible by 5, print x.
# 5. Increment x by 1 in each iteration.
# 6. Repeat until x becomes greater than N.

# CODE
n = int(input("Enter number: "))
x = 1

while x <= n:
    if x % 5 == 0:
        print(x)
    x += 1
