"""
CP1404/CP5632 - guitar test
"""
from Pracs.prac_06.guitar import Guitar

another_guitar = Guitar("Another guitar", 2013, 1000)
guitar = Guitar("Gibson L-5 CES", 1922, 16035)

print(f"{guitar.name} get_age() - Expected 100. Got {guitar.get_age()}")
print(f"{another_guitar.name} get_age() - Expected 9. Got {another_guitar.get_age()}")

print(f"{guitar.name} is_vintage() - Expected True. Got {guitar.is_vintage()}")
print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")
