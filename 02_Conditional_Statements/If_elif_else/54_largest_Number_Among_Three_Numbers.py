"""
Program: Find Largest Number Among Three Numbers
Author: Hema
Concepts Used: Variables, Input, Type Casting, if-elif-else,
Logical Operator (and), Comparison Operators (>, ==), Multiple Conditions, Output
Description: Accepts three numbers from the user and identifies the largest
number. It also handles cases where two or all three numbers are equal.
"""

# LOGIC
# Accept three numbers from the user.
# Check whether the first number is greater than the other two.
# Check whether the second number is greater than the other two.
# Check whether the third number is greater than the other two.
# Check whether any two numbers are equal and larger than the third.
# If none of the above conditions are true, all three numbers are equal.
# Display the appropriate result.


# CODE
num1 = float(input("Enter first Number: "))
num2 = float(input("Enter second Number: "))
num3 = float(input("Enter Third number: "))

if num1 > num2 and num1 > num3:
    print("First number is larger:", num1)

elif num2 > num1 and num2 > num3:
    print("Second number is larger:", num2)

elif num3 > num1 and num3 > num2:
    print("Third number is larger:", num3)

elif num1 == num2 and num1 > num3:
    print("First and Second numbers are larger")

elif num1 == num3 and num1 > num2:
    print("First and Third numbers are larger")

elif num2 == num3 and num2 > num1:
    print("Second and Third numbers are larger")

else:
    print("All numbers are equal")
