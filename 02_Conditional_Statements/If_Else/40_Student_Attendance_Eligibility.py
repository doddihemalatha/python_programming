"""
Program: Student Attendance Eligibility Checker
Author: Hema
Concepts Used: Variables, Input, Type Casting, Comparison Operator (>=), if-else, Output
Description: Accepts a student's attendance percentage and checks whether the student is allowed to write the exam based on the 75% attendance requirement.
"""

# LOGIC
# Accept the student's attendance percentage.
# Check whether attendance is 75% or above.
# If attendance is 75% or above, allow the student to write the exam.
# Otherwise, do not allow the student to write the exam.


# CODE
student_attendance = float(input("Enter Student Attendance Percentage: "))

if student_attendance >= 75:
    print("\nAllowed to Write Exam")
else:
    print("\nNot Allowed")
