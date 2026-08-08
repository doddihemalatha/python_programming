"""
Program : Swap Two Numbers using multiple assignment
Author  : Hemalatha

Concepts Used:
- Variables
- Input
- Type Casting
- Multiple Assignment
- Output

Description:
Swaps the values of two variables without using a third variable.
"""

#LOGIC
# Accept two numbers from the user.
# Swap the values using multiple assignment.
# Display the swapped values.

#CODE
num1 = int(input("Enter first Number : "))
num2 = int(input("Enter second Number : "))

num1 = num1 + num2
num2 = num1 - num2
num1 = num1- num2

print("-"*20)
print("First Number is:",num1)
print("Second Number is:",num2)
