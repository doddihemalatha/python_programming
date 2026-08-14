"""
Program : Integer Input Type Casting
Author  : Hemalatha

Concepts Used:
- input()
- Type Casting
- int()
- Variables
- Arithmetic Operator (+)
- Output

Description:
Accepts two numbers from the user, converts them from strings
to integers, and performs addition.
"""

# Logic
# Accept two values from the user.
# Convert the input values from string to integer using int().
# Add the two integers.
# Display the result.

#code
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

result = num1 + num2

print("Addition =", result)
