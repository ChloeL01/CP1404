"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    - It will occur if a non integer value is entered e.g. a string

2. When will a ZeroDivisionError occur?
    - It will occur if the denominator entered is a 0 as the numerator is not divisible by 0

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    - Yes, add an if statement to check if the denominator is 0 then get input again
"""

# New - with if statement instead
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

except ValueError:
    print("Numerator and denominator must be valid numbers!")

if denominator == 0:
    print("Cannot be 0, try again!")
else:
    fraction = numerator / denominator
    print(fraction)
print("Finished.")


# original - with ZeroDivisionError exception
# try:
#     numerator = int(input("Enter the numerator: "))
#     denominator = int(input("Enter the denominator: "))
#     fraction = numerator / denominator
#     print(fraction)
# except ValueError:
#     print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# print("Finished.")
