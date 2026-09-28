"""
Program: Compare Two Numbers
Author: Hema
Concepts Used: Variables, Input, Type Casting, if-elif-else,
Comparison Operators (>, ==), Output
Description: Accepts two numbers from the user and compares them.
The program identifies which number is larger or checks whether
both numbers are equal.
"""

# LOGIC
# Accept two numbers from the user.
# Compare the first number with the second number.
# If the first number is greater, display the first number.
# Otherwise, check whether the second number is greater.
# If neither number is greater, both numbers must be equal.
# Display the result.


# CODE
num1 = float(input("Enter first Number: "))
num2 = float(input("Enter second Number: "))

if num1 > num2:
    print("First number", num1, "is larger")

elif num2 > num1:
    print("Second number", num2, "is larger")

else:
    print("Both Numbers are Equal")
