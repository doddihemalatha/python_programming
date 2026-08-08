"""
Program : Area of Circle
Author  : Hemalatha

Concepts Used:
- Variables
- Input
- Type Casting
- Arithmetic Operators (*, **)
- Output

Description:
Accepts the radius of a circle and calculates its area.
"""

#LOGIC
# Accept the radius of the circle.
# Calculate the square of the radius.
# Multiply it by pie.
# Store the result.
# Display the area.

#CODE
radius = float(input("Enter Radius : "))

pie = 3.14
area = pie*(radius**2)
print("Area of Circle : ",area)
