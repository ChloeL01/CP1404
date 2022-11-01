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
    for guitar in guitars:
        print(guitar)


if __name__ == '__main__':
    main()
