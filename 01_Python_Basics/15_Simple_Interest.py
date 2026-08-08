"""
Program : Simple Interest
Author  : Hemalatha

Concepts Used:
- Variables
- Input
- Type Casting
- Arithmetic Operators (*, /)
- Output

Description:
Accepts principal amount, rate of interest, and time,
then calculates the simple interest.
"""

#LOGIC
# Accept the principal amount, rate, and time.
# Multiply principal, rate, and time.
# Divide the result by 100.
# Store the simple interest.
# Display the result.

#CODE
principal = float(input("Enter Principal Amount : "))
rate = float(input("Enter Rate of Interest : "))
time = float(input("Enter Time in years: "))

si = principal * rate * time/100
print("Simple Interest is : ",si)
