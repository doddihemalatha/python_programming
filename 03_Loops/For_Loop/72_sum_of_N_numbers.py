"""
Program: Find the Sum of Numbers from 1 to N
Author: Hema
Concepts Used: For Loop, range(), input(), int(), print()
Description: Calculates the sum of all numbers from 1 to N using a for loop.
"""

# LOGIC
# 1. Get the value of N from the user.
# 2. Initialize total to 0.
# 3. Use a for loop to iterate through numbers from 1 to N.
# 4. Add each number to total.
# 5. Print the final sum.

# CODE
n = int(input("Enter N: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Sum =", total)
