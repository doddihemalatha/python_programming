"""
Program: Print Numbers from N to 1
Author: Hema
Concepts Used: For Loop, range(), input(), int(), print()
Description: Prints numbers from N down to 1 using a for loop.
"""

# LOGIC
# 1. Get the value of N from the user.
# 2. Use range(N, 0, -1) to generate numbers from N down to 1.
# 3. Iterate through each number using a for loop.
# 4. Print each number.

# CODE
n = int(input("Enter N: "))

for i in range(n, 0, -1):
    print(i)
