"""
Program: Find the Sum of Even Numbers from 1 to N
Author: Hema
Concepts Used: While Loop, if statement, Modulus Operator, Variables, Arithmetic Operators, input(), int(), print()
Description: Calculates the sum of all even numbers from 1 to N using a while loop.
"""

# LOGIC
# 1. Get a number from the user.
# 2. Initialize i to 1 and sums to 0.
# 3. Check whether i is less than or equal to N.
# 4. If i is divisible by 2, add i to sums.
# 5. Increment i by 1 in each iteration.
# 6. Repeat until i becomes greater than N.
# 7. Print the sum of even numbers.

# CODE
n = int(input("Enter a number: "))

i = 1
sums = 0

while i <= n:
    if i % 2 == 0:
        sums = sums + i
    i += 1

print("Sum of even numbers =", sums)
