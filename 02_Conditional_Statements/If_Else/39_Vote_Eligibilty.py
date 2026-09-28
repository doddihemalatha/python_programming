"""
Program: Voting Eligibility Checker
Author: Hema
Concepts Used: Variables, Input, Type Casting, Comparison Operator (>=),
if-else, Output
Description: Accepts a person's age and checks whether they meet
the age requirement for voting.
"""

# LOGIC
# Accept the person's age.
# Check whether the age is 18 or above.
# If yes, display "Eligible to Vote".
# Otherwise, display "Not Eligible to Vote".

# CODE
age = int(input("Enter Your Age: "))

if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")
