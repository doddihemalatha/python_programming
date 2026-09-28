"""
Program: Arithmetic Operations on Two Numbers
Author: Hema
Concepts Used: Variables, Input, Type Casting, Arithmetic Operators (+, -, *, /), Output
Description: Accepts two numbers from the user and performs addition, subtraction,
multiplication, and division using arithmetic operators.
"""

# LOGIC
# Accept two numbers from the user.
# Perform addition, subtraction, multiplication, and division.
# Store each result in a separate variable.
# Display all the results.


# CODE
first_no = float(input("Enter first number: "))
second_no = float(input("Enter second number: "))

addition = first_no + second_no
subtraction = first_no - second_no
multiplication = first_no * second_no
division = first_no / second_no

print("Addition is:", addition)
print("Subtraction is:", subtraction)
print("Multiplication is:", multiplication)
print("Division is:", division)
