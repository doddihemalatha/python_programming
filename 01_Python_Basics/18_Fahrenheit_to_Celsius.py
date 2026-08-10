"""
Program : Fahrenheit to Celsius
Author  : Hemalatha

Concepts Used:
- Variables
- Input
- Type Casting
- Arithmetic Operators (-, *, /)
- Output

Description:
Accepts temperature in Fahrenheit and converts it to Celsius.
"""

# Logic
# Accept the temperature in Fahrenheit.
# Subtract 32 from Fahrenheit.
# Multiply the result by 5/9.
# Store the Celsius temperature.
# Display the result.

#code
fahrenheit = float(input("Enter Temperature in Fahrenheit : "))
celsius = (5/9)*(fahrenheit-32)
print("Temperature in Celsius : ",celsius)
