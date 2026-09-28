"""
Program: Simple Login System
Author: Hema
Concepts Used: Variables, Input, String Comparison, if-else,
Equality Operator (==), Output
Description: Accepts a password from the user and compares it with
the stored password. If both passwords match, login is successful;
otherwise, the login fails.
"""

# LOGIC
# Store the actual password.
# Ask the user to enter a password.
# Compare the entered password with the actual password.
# If both passwords match, display "Login Successfully".
# Otherwise, display "Wrong Password".


# CODE
actual_password = "0007"

password = input("Enter Password: ")

if password == actual_password:
    print("Login Successfully")
else:
    print("Wrong Password")
