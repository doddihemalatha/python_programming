"""
Program: Print Numbers in a Given Range
Author: Hema
Concepts Used: For Loop, range(), input(), int(), print()
Description: Prints all numbers between a starting number and an ending number using a for loop.
"""

# LOGIC
# 1. Get the starting number from the user.
# 2. Get the ending number from the user.
# 3. Use range(start, end + 1) to generate numbers within the range.
# 4. Iterate through each number using a for loop.
# 5. Print each number.

# CODE
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for i in range(start, end + 1):
    print(i)
  
