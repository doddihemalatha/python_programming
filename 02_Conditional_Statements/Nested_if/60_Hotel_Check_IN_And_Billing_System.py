"""
Program: Hotel Check-in and Billing System
Author: Hema
Concepts Used: Variables, Input, Type Casting, Nested if-else,
Comparison Operators (>=), Arithmetic Operators (*),
String Methods, Conditional Statements, Output
Description: Checks guest age and ID, calculates the room bill
based on the number of days stayed, and offers free breakfast
when the bill reaches the specified amount.
"""

# LOGIC
# Accept the guest's age.
# Check whether the guest is at least 18 years old.
# If eligible, ask whether the guest has an ID.
# If the guest has an ID, accept the number of days stayed.
# Set the room charge per day to 1500.
# Calculate and display the total room bill.
# If the bill is 10000 or more, offer free breakfast.
# If the guest has no ID, reject check-in.
# Handle invalid ID responses.
# If the guest is under 18, do not allow check-in.

# CODE

age = int(input("Enter Your Age: "))

if age >= 18:
    has_id = input("Do you have ID: ").lower()

    if has_id == 'yes':
        no_of_days = int(input("Enter Number of days: "))

        room_charge = 1500
        total_room_charge = no_of_days * room_charge

        print("-" * 20)
        print("Check-in Successful")
        print("Days Stayed:", no_of_days)
        print("Room Charge per day:", room_charge)
        print("Total Bill:", total_room_charge)

        if total_room_charge >= 10000:
            print("Congratulations!\nFree Breakfast Included")

    elif has_id == 'no':
        print("Check-in Rejected\nValid ID Required")

    else:
        print("Invalid")

else:
    print("Check-in Not Allowed")
