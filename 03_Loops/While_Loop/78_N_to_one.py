"""
Program: Print Numbers from N to 1
Author: Hema
Concepts Used: While Loop, Variables, Comparison Operator, Decrement Operator, input(), int(), print()
Description: Prints numbers from the given number down to 1 using a while loop.
"""

# LOGIC
# 1. Get a number from the user.
# 2. Check whether the number is greater than or equal to 1.
# 3. If the condition is true, print the number.
# 4. Decrease the number by 1 in each iteration.
# 5. Repeat until the number becomes less than 1.

# CODE
num = int(input("Enter Number: "))

while num >= 1:
    print(num)
    num = num - 1
