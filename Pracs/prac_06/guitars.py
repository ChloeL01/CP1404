"""
CP1404/CP5632 - guitars program
"""
from Pracs.prac_06.guitar import Guitar

guitars = []

print("My guitars!")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print(guitar, "added")
    name = input("Name: ")

# test formatting with these
guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

print("These are my guitars: ")
for i, guitar in enumerate(guitars, 1):
    vintage_string = " (vintage)" if Guitar.is_vintage(guitar) else ""
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
