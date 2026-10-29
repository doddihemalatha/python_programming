"""
Program: Loan Eligibility Checker
Author: Hema
Concepts Used: Variables, Input, Type Casting, Nested if-else,
Comparison Operators (>=), Multiple Conditions, Output
Description: Checks loan eligibility based on age, salary,
and credit score.
"""

# LOGIC
# Accept the applicant's age.
# Check whether the applicant is at least 21 years old.
# If eligible by age, ask for the salary.
# Check whether the salary is at least 30,000.
# If eligible by salary, ask for the credit score.
# Check whether the credit score is at least 750.
# Approve the loan if all conditions are satisfied.
# Otherwise, display the appropriate rejection message.

# CODE

age = int(input("Enter your Age: "))

if age >= 21:
    salary = int(input("Enter your Salary: "))

    if salary >= 30000:
        credit_score = int(input("Enter Your Credit Score: "))

        if credit_score >= 750:
            print("Congratulations! \nLoan Approved")
        else:
            print("Loan Rejected \nLow Credit Score")

    else:
        print("Loan Rejected \nSalary should be at least 30,000")

else:
    print("Not Eligible \nAge should be 21 or above")
