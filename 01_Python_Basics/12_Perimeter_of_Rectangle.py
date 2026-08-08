"""
Program : Perimeter of Rectangle
Author  : Hema

Concepts Used:
- Variables
- Input
- Type Casting
- Arithmetic Operators (+, *)
- Output

Description:
Accepts the length and breadth of a rectangle and calculates its perimeter.
"""

#LOGIC
# Accept the length and breadth from the user.
# Add the length and breadth.
# Multiply the sum by 2.
# Store the result.
# Display the perimeter.

#CODE
length = int(input("Enter Length: "))
breadth = int(input("Enter Breadth: "))

perimeter = 2 * (length + breadth)

print("Perimeter of Rectangle =", perimeter)
