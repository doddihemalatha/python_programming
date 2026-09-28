"""
Program: Electricity Bill Calculator
Author: Hema
Concepts Used: Variables, Input, Type Casting, if-elif-else,
Comparison Operators (<, <=), Arithmetic Operator (*),
Range Checking, Input Validation, Output
Description: Calculates the electricity bill based on the number
of units consumed. Different rates are applied depending on
the unit range.
"""

# LOGIC
# Accept the number of electricity units consumed.
# If units are negative, display "Invalid Units".
# If units are 100 or below, the rate is 0 per unit.
# If units are between 101 and 300, the rate is 5 per unit.
# If units are above 300, the rate is 8 per unit.
# Calculate and display the electricity bill.

# CODE
units = int(input("Enter Units: "))

if units < 0:
    print("Invalid Units")

elif units <= 100:
    electricity_bill = units * 0
    print("Electricity Bill:", electricity_bill)

elif units <= 300:
    electricity_bill = units * 5
    print("Electricity Bill:", electricity_bill)

else:
    electricity_bill = units * 8
    print("Electricity Bill:", electricity_bill)
