"""
Program: Membership Eligibility Checker
Author: Hema
Concepts Used: Variables, Input, Type Casting, String Methods,
if-elif-else, Comparison Operators, Logical Operator (and),
Input Validation, Output
Description: Checks whether a person is eligible for membership
based on age and availability of a medical certificate.
"""

# LOGIC
# Accept the user's age.
# Ask whether the user has a medical certificate.
# Convert the certificate input to lowercase.
# If age is below 16, the person is not eligible.
# If age is 16 or above and has a certificate, approve membership.
# If age is 16 or above and does not have a certificate,
# ask the person to bring one.
# Handle invalid certificate input.

# CODE

age = int(input("Enter your Age: "))

medical_certificate = input("Do you have a Medical Certificate Yes/No: ").lower()

if age < 16:
    print("Not Eligible")

elif age >= 16 and medical_certificate == "yes":
    print("Membership Approved")

elif age >= 16 and medical_certificate == "no":
    print("Bring Medical Certificate")

else:
    print("Invalid")
