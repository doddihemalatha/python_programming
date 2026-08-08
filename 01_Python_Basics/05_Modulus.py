"""
Program : Modulus of Two Numbers
Author  : Hemalatha

Concepts Used:
- Variables
- Input
- Type Casting
- Arithmetic Operator (%)
- Output

Description:
Accepts two numbers from the user and finds the remainder
after dividing the first number by the second number.
"""

#LOGIC
# Accept two numbers
# divide the first number by the second number
# find the remainder by using the operator %
# store the remainder
# Display the result.

#CODE
num1 = int(input("Enter first Number:"))
num2 = int(input("Enter second Number:"))

result = num1 % num2
print("The remainder is ",result)
