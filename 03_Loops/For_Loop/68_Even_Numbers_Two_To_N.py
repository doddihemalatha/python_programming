"""
Program: Print Even Numbers from 2 to N
Author: Hema
Concepts Used: For Loop, range(), input(), int(), print()
Description: Prints all even numbers from 2 to N using a for loop.
"""

# LOGIC
# 1. Get the value of N from the user.
# 2. Use range(2, N + 1, 2) to generate even numbers from 2 to N.
# 3. Iterate through each even number using a for loop.
# 4. Print each even number.

# CODE
n = int(input("Enter N: "))

for i in range(2, n + 1, 2):
    print(i)
