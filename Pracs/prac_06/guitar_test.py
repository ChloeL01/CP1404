"""
CP1404/CP5632 - guitar test
"""
from Pracs.prac_06.guitar import Guitar


def main():
    """Test various class calls and formatting for guitar information"""
    other = Guitar("Another guitar", 2013, 1000)
    guitar = Guitar("Gibson L-5 CES", 1922, 16035)

    print(f"{guitar.name} get_age() - Expected 100. Got {guitar.get_age()}")
    print(f"{other.name} get_age() - Expected 9. Got {other.get_age()}")

    print(f"{guitar.name} is_vintage() - Expected True. Got {guitar.is_vintage()}")
    print(f"{other.name} is_vintage() - Expected False. Got {other.is_vintage()}")


if __name__ == '__main__':
    main()
