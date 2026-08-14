"""
Program : Float Input Type Casting
Author  : Hemalatha

Concepts Used:
- input()
- Type Casting
- float()
- Variables
- Arithmetic Operator (+)
- Output

Description:
Accepts two decimal numbers from the user, converts them
from strings to float values, and performs addition.
"""

# Logic
# Accept two values from the user.
# Convert the input values from string to float using float().
# Add the two float values.
# Display the result.

#code
num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

result = num1 + num2

print("Addition =", result)
