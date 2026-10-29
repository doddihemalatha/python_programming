"""
Program: Print Multiples of 5 up to N
Author: Hema
Concepts Used: For Loop, range(), input(), int(), print()
Description: Prints all multiples of 5 up to N using a for loop.
"""

# LOGIC
# 1. Get the value of N from the user.
# 2. Use range(5, N + 1, 5) to generate multiples of 5 up to N.
# 3. Iterate through each multiple using a for loop.
# 4. Print each multiple.

# CODE
n = int(input("Enter N: "))

for i in range(5, n + 1, 5):
    print(i)
