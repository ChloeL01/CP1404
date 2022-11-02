"""
CP1404/CP5632 Practical - my guitars

"""
from Pracs.prac_06.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Load guitars from the file."""
    guitars = []
    # open file formatted like: name,year,cost
    with open(FILENAME, "r") as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)
    guitars.sort()
    print("Guitars from file: ")
    for guitar in guitars:
        print(guitar)

    # part 2
    print("")
    print("Enter new guitars")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added")
        print("")
        name = input("Name: ")

    print(f"Guitars saved to {FILENAME}")
    with open(FILENAME, "w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", end="\n", file=out_file)


if __name__ == '__main__':
    main()
