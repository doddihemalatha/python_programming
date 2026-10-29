"""
Program: Print Numbers from 1 to N
Author: Hema
Concepts Used: For Loop, range(), input(), int(), print()
Description: Prints numbers from 1 to N using a for loop.
"""

# LOGIC
# 1. Get the value of N from the user.
# 2. Use range(1, N + 1) to generate numbers from 1 to N.
# 3. Iterate through each number using a for loop.
# 4. Print each number.

# CODE
n = int(input("Enter N: "))

for i in range(1, n + 1):
    print(i)
