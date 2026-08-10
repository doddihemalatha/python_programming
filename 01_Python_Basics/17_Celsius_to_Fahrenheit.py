"""
Program : Celsius to Fahrenheit
Author  : Hemalatha

Concepts Used:
- Variables
- Input
- Type Casting
- Arithmetic Operators (*, /, +)
- Output

Description:
Accepts temperature in Celsius and converts it to Fahrenheit.
"""

# Logic
# Accept the temperature in Celsius.
# Multiply Celsius by 9/5.
# Add 32 to the result.
# Store the Fahrenheit temperature.
# Display the result.

#Code
celsius = float(input("Enter Temperatue in Celsius : "))
fahrenheit = (9/5)*(celsius+32)
print('Temperature in Fahrenheit : ',fahrenheit)
