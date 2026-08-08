"""
Program : Swap Two Numbers Using Third Variable
Author  : Hema

Concepts Used:
- Variables
- Input
- Type Casting
- Assignment Operator (=)
- Output

Description:
Swaps the values of two variables using a third temporary variable.
"""

#LOGIC
# Accept two numbers from the user.
# Store the first value in a temporary variable.
# Assign the second value to the first variable.
# Assign the temporary value to the second variable.
# Display the swapped values

#CODE
num1 = int(input("Enter first Number : "))
num2 = int(input("Enter second Number : "))

temp = num1
num1 = num2
num2 = temp

print("-"*20)
print("After Swapping")
print("First Number :",num1)
print("Second Number :",num2)
