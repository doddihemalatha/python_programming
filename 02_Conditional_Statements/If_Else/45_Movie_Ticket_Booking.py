"""
Program: Movie Ticket Booking and Popcorn Offer
Author: Hema
Concepts Used: Variables, Input, Type Casting, Arithmetic Operators (*),
if-else, Comparison Operator (>=), Output
Description: Calculates the total movie ticket price based on the number
of tickets and checks whether the customer qualifies for free popcorn.
"""

# LOGIC
# Set the price of one movie ticket.
# Accept the number of tickets from the user.
# Calculate the total ticket price.
# Check whether the total price is 1000 or more.
# If yes, provide free popcorn.
# Otherwise, display that there is no free popcorn.
# Display the total bill.


# CODE
ticket_price = 200

no_of_tickets = int(input("Enter Number of Tickets: "))

total_price = ticket_price * no_of_tickets

if total_price >= 1000:
    print("Congratulations!\nYou got free popcorn")
else:
    print("No Free Popcorn")

print("Total Bill:", total_price)
