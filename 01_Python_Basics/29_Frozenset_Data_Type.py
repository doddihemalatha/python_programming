"""
Program : Frozenset Data Type
Author  : Hema

Concepts Used:
- Frozenset
- Variables
- type()
- Output
- Unique values
- Immutable collection

Description:
Demonstrates how to store unique values in a frozenset
and identify its data type.
"""

# Logic
# Create a frozenset with multiple values.
# Duplicate values are automatically removed.
# Check its data type using type().
# Display the frozenset.

#code
num = frozenset([10,20,30,10,20])

print("Frozenset : ",num)
print("Data Type : ",type(num))
