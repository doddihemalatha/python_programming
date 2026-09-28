"""
Program: Student Marks Grade Calculator
Author: Hema
Concepts Used: Variables, Input, Type Casting, if-elif-else,
Logical Operator (or), Comparison Operators (<, >, >=), Range Checking, Output
Description: Accepts a student's marks and assigns a grade based on the
marks obtained. It also checks whether the entered marks are within
the valid range of 0 to 100.
"""

# LOGIC
# Accept the student's marks.
# Check whether the marks are below 0 or above 100.
# If yes, display "Invalid Marks".
# Otherwise, check the marks against each grade range.
# 90 or above → Grade A
# 75 to 89 → Grade B
# 50 to 74 → Grade C
# 35 to 49 → Grade D
# Below 35 → Fail
# Display the appropriate result.


# CODE
marks = int(input("Enter your Marks: "))

if marks < 0 or marks > 100:
    print("Invalid Marks")

elif marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 50:
    print("Grade C")

elif marks >= 35:
    print("Grade D")

else:
    print("Fail")
