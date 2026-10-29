"""
Program: Age and ID Entry Checker
Author: Hema
Concepts Used: Variables, Input, Type Casting, String Methods,
Nested if-else, Comparison Operators, Input Validation, Output
Description: Checks whether a person meets the age requirement
and has valid ID proof before allowing entry.
"""

# LOGIC
# Accept the person's age.
# Check whether the person is 18 or older.
# If eligible by age, ask whether they have an ID.
# If the answer is yes, allow entry.
# If the answer is no, ask them to bring ID proof.
# If the answer is neither yes nor no, display an error.
# If the person is under 18, display "Not Eligible".

# CODE

age = int(input("Enter Your Age: "))

if age >= 18:
    had_id = input("Do you have ID: ").lower()

    if had_id == 'yes':
        print("Entry Allowed")

    elif had_id == 'no':
        print("Bring ID Proof")

    else:
        print("Invalid. Enter only yes or no")

else:
    print("Not Eligible")
