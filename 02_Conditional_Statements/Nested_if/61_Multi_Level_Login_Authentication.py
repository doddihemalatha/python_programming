"""
Program: Multi-Level Login Authentication System
Author: Hema
Concepts Used: Variables, Input, Type Casting, String Methods,
Nested if-else, Comparison Operators (==), Authentication Logic,
Output
Description: Simulates a login system by validating the username,
password, and OTP in sequence before allowing access.
"""

# LOGIC
# Accept the username and convert it to lowercase.
# Check whether the username matches the stored username.
# If correct, ask for the password.
# Check whether the password is correct.
# If correct, ask for the OTP.
# Check whether the OTP matches the stored OTP.
# If all three credentials are correct, display login success.
# Otherwise, display the appropriate error message.

# CODE

username = input("Enter your Name: ").lower()

if username == 'hema':
    password = input("Enter Password: ")

    if password == 'python123':
        otp = int(input("Enter OTP: "))

        if otp == 5678:
            print("Login Successful")
        else:
            print("Invalid OTP")

    else:
        print("Wrong Password")

else:
    print("Invalid Username")
