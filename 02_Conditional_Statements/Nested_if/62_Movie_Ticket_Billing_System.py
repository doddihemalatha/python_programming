"""
Program: Movie Ticket Billing System
Author: Hema
Concepts Used: Variables, Input, Type Casting, if-elif-else,
Nested if, Logical Operators (and, or), Comparison Operators,
Arithmetic Operators (*), Input Validation, Output
Description: Calculates movie ticket prices based on the customer's
age and number of tickets, validates the inputs, and checks
eligibility for a free popcorn offer.
"""

# LOGIC
# Set the adult and child ticket prices.
# Accept the customer's age and number of tickets.
# If age or number of tickets is invalid, display "Invalid".
# If the customer is below 5 years old, provide a free ticket.
# If the customer is between 5 and 17, apply the child ticket price.
# Otherwise, apply the adult ticket price.
# Calculate and display the total ticket price.
# If the total price is 1000 or more, offer free popcorn.

# CODE

adult_ticket_price = 200
child_ticket_price = 100

age = int(input("Enter Your Age: "))
no_of_tickets = int(input("Enter Number of Tickets: "))

if age <= 0 or no_of_tickets <= 0:
    print("Invalid")

elif age < 5:
    print("Free Ticket")

elif age >= 5 and age <= 17:
    print("Child Ticket:", child_ticket_price)

    total_price = no_of_tickets * child_ticket_price
    print("Total Price:", total_price)

    if total_price >= 1000:
        print("Congratulations! You got FREE Popcorn.")

else:
    print("Adult Ticket:", adult_ticket_price)

    total_price = no_of_tickets * adult_ticket_price
    print("Total Price:", total_price)

    if total_price >= 1000:
        print("Congratulations! You got FREE Popcorn.")
