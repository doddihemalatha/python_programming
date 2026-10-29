"""
Program: Count the Frequency of Each Word in a Sentence
Author: Hema
Concepts Used: For Loop, if-else, split(), Dictionary
Description: Counts how many times each word appears in a sentence and stores the frequencies in a dictionary.
"""

# LOGIC
# 1. Get a sentence from the user.
# 2. Use split() to separate the sentence into individual words.
# 3. Create an empty dictionary to store word frequencies.
# 4. Iterate through each word using a for loop.
# 5. If the word already exists in the dictionary, increase its count by 1.
# 6. Otherwise, add the word to the dictionary with a count of 1.
# 7. Print the dictionary containing each word and its frequency.

# CODE
text = input("Enter a sentence: ")
words = text.split()
freq = {}

for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1

print(freq)
