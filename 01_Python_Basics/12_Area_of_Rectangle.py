"""
Program : Area of Rectangle
Author  : Hemalatha

Concepts Used:
- Variables
- Input
- Type Casting
- Arithmetic Operator (*)
- Output

Description:
Accepts the length and breadth of a rectangle and calculates its area.
"""

#LOGIC
# Accept the length and breadth from the user.
# Multiply length by breadth.
# Store the result.
# Display the area.

#CODE
length = int(input("Enter Length : "))
width = int(input("Enter width : "))

area = length * width
print("Area of Rectangle : ",area)
