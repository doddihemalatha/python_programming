"""
Program : Convert Days into Years, Months and Days
Author  : Hemalatha

Concepts Used:
- Variables
- Input
- Type Casting
- Arithmetic Operators (//, %)
- Output

Description:
Accepts the total number of days and converts them into
years, months, and remaining days.
"""

# Logic
# Accept the total number of days.
# Find the number of complete years using //.
# Find the remaining days using %.
# Convert the remaining days into complete months.
# Find the remaining days after months.
# Display years, months, and days.

#code
total_days = int(input("Enter Total days : "))

year = total_days // 365
remaining_days = total_days % 365

month = remaining_days // 30
days = remaining_days % 30

print("Year : ",year)
print("Month : ",month)
print("Days : ",days)
