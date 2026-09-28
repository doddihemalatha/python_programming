"""
Program: Character Type Checker
Author: Hema
Concepts Used: Variables, Input, String Methods, len(),
if-elif-else, Comparison Operator (!=), Output
Description: Accepts a character from the user and checks whether
it is an alphabet, digit, or special character. The program also
validates that exactly one character is entered.
"""

# LOGIC
# Accept input from the user.
# Check whether the input contains exactly one character.
# If not, display "Invalid".
# If the character is an alphabet, display "Alphabet".
# If the character is a digit, display "Digit".
# Otherwise, classify it as a special character.

# CODE
character = input("Enter character: ")

if len(character) != 1:
    print("Invalid")
elif character.isalpha():
    print("Alphabet")
elif character.isdigit():
    print("Digit")
else:
    print("Special Character")
