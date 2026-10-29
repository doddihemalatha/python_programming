"""
Program: Print Odd Numbers from 1 to N
Author: Hema
Concepts Used: While Loop, Variables, Comparison Operator, Increment Operator, input(), int(), print()
Description: Prints all odd numbers from 1 to N using a while loop.
"""

# LOGIC
# 1. Get the ending number from the user.
# 2. Initialize x to 1.
# 3. Check whether x is less than or equal to the ending number.
# 4. If the condition is true, print x.
# 5. Increment x by 2 in each iteration.
# 6. Repeat until the condition becomes false.

# CODE
num = int(input("Enter End Number: "))
x = 1

while x <= num:
    print(x)
    x += 2
