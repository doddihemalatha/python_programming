"""
Program: ATM Withdrawal Validation System
Author: Hema
Concepts Used: Variables, Input, Type Casting, if-elif-else,
Comparison Operators, Modulus Operator (%), Arithmetic Operators,
Input Validation, Output
Description: Validates the withdrawal amount before processing
an ATM transaction and calculates the remaining balance.
"""

# LOGIC
# Set the initial account balance.
# Take the withdrawal amount as input.
# Check if the withdrawal amount is valid.
# Check if sufficient balance is available.
# Check if the withdrawal amount is a multiple of 100.
# If all conditions are valid, process the withdrawal.
# Calculate and display the remaining balance.

# CODE

initial_balance = 10000

withdraw_amount = int(input("Enter Withdraw Amount: "))

if withdraw_amount <= 0:
    print("Invalid Amount")

elif initial_balance < withdraw_amount:
    print("Insufficient Balance")

elif withdraw_amount % 100 != 0:
    print("Enter Amount in multiples of 100")

else:
    print("-" * 20)
    print("Withdrawal Successful")

    remaining_balance = initial_balance - withdraw_amount

    print("Remaining Balance:", remaining_balance)
