"""
Program : Average of 3 Numbers
Author  : Hemalatha

Concepts Used:
- Variables
- Input
- Type Casting
- Arithmetic Operators (+, /)
- Output

Description:
Accepts three numbers from the user and calculates their average.
"""

#LOGIC
# Accept three numbers from the user.
# Add the three numbers.
# Divide the sum by 3.
# Store the average.
# Display the result

#CODE
num1 = int(input("Enter first Number:"))
num2 = int(input("Enter second Number:"))
num3 = int(input("Enter Third Number:"))

total = num1 + num2 + num3
average = total/3
print("Average of 3 number is:",average)
