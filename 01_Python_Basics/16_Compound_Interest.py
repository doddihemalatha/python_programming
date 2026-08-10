"""
Program : Compound Interest
Author  : Hemalatha

Concepts Used:
- Variables
- Input
- Type Casting
- Arithmetic Operators (*, -, /)
- Exponent Operator (**)
- Output

Description:
Accepts the principal amount, rate of interest, and time,
then calculates the compound interest.
"""

#LOGIC
# Accept the principal amount, rate, and time.
# Calculate the amount using the compound interest formula.
# Subtract the principal from the amount.
# Store the compound interest.
# Display the result.

#CODE
principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time (in years): "))

amount = principal * (1 + rate / 100) ** time
compound_interest = amount - principal

print("Compound Interest =", compound_interest)
