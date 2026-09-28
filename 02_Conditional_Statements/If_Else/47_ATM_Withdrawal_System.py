"""
Program: ATM Withdrawal System
Author: Hema
Concepts Used: Variables, Input, Type Casting, if-else,
Comparison Operator (<=), Arithmetic Operator (-), Output
Description: Checks whether the requested withdrawal amount
is within the available balance and calculates the remaining balance.
"""

# LOGIC
# Set the available account balance.
# Accept the withdrawal amount.
# Check whether the withdrawal amount is less than or equal to the balance.
# If yes, subtract the withdrawal amount from the balance.
# Otherwise, display "Insufficient Balance".

# CODE
fixed_balance = 10000

withdraw = int(input("Enter Withdraw Amount: "))

if withdraw <= fixed_balance:
    print("Withdrawal Successful")

    remaining_balance = fixed_balance - withdraw
    print("Remaining Balance:", remaining_balance)

else:
    print("Insufficient Balance")
