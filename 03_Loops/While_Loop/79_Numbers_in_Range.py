"""
Program: Print Numbers in a Given Range
Author: Hema
Concepts Used: While Loop, Variables, Comparison Operator, Increment Operator, input(), int(), print()
Description: Prints all numbers from the starting number to the ending number using a while loop.
"""

# LOGIC
# 1. Get the starting number from the user.
# 2. Get the ending number from the user.
# 3. Check whether the starting number is less than or equal to the ending number.
# 4. If the condition is true, print the starting number.
# 5. Increment the starting number by 1.
# 6. Repeat until the condition becomes false.

# CODE
num1 = int(input("Enter Start Number: "))
num2 = int(input("Enter End Number: "))

while num1 <= num2:
    print(num1)
    num1 += 1
