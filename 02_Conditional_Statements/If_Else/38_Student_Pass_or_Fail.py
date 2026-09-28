"""
Program: Student Pass or Fail Checker
Author: Hema
Concepts Used: Variables, Input, Type Casting, Comparison Operator (>=),
if-else, Output
Description: Accepts a student's marks and checks whether the student
has achieved the minimum passing marks of 35.
"""

# LOGIC
# Accept the student's marks.
# Check whether the marks are 35 or above.
# If yes, display "Pass".
# Otherwise, display "Fail".

# CODE
marks = float(input("Enter Student Marks: "))

if marks >= 35:
    print("Pass")
else:
    print("Fail")
