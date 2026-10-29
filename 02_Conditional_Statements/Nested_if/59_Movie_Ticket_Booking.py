"""
Program: Movie Ticket Booking and Popcorn Offer
Author: Hema
Concepts Used: Variables, Input, Type Casting, if-else,
Comparison Operators (>=), Arithmetic Operators (*),
Conditional Statements, Output
Description: Calculates the total movie ticket bill and
checks whether the customer qualifies for a free popcorn offer.
"""

# LOGIC
# Set the price of one movie ticket.
# Accept the number of tickets.
# Calculate the total ticket price.
# If the total price is 1000 or more, offer free popcorn.
# Otherwise, display that no free popcorn is available.
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
