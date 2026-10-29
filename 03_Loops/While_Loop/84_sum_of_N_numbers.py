"""
Program: Find the Sum of Numbers from 1 to N
Author: Hema
Concepts Used: While Loop, Variables, Arithmetic Operators, Comparison Operator, input(), int(), print()
Description: Prints numbers from 1 to N and calculates their sum using a while loop.
"""

# LOGIC
# 1. Get a number from the user.
# 2. Initialize x to 1 and total to 0.
# 3. Check whether x is less than or equal to N.
# 4. If the condition is true, print x.
# 5. Add x to total.
# 6. Increment x by 1 in each iteration.
# 7. Repeat until x becomes greater than N.
# 8. Print the final sum.

# CODE
num = int(input("Enter Number: "))

x = 1
total = 0

while x <= num:
    print(x)
    total = total + x
    x += 1

print("Sum:", total)
