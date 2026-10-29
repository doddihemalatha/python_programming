"""
Program: Find the Sum of Even Numbers from 1 to N
Author: Hema
Concepts Used: For Loop, range(), input(), int(), print()
Description: Calculates the sum of all even numbers from 1 to N using a for loop.
"""

# LOGIC
# 1. Get the value of N from the user.
# 2. Initialize total to 0.
# 3. Use range(2, N + 1, 2) to generate even numbers from 2 to N.
# 4. Add each even number to total.
# 5. Print the final sum.

# CODE
n = int(input("Enter N: "))
total = 0

for i in range(2, n + 1, 2):
    total += i

print("Sum of even numbers =", total)
