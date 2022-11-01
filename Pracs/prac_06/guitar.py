"""CP1404/CP5632 Practical - Guitar class"""

CURRENT_YEAR = 2022
VINTAGE_AGE = 50


class Guitar:
    """Represent a guitar object"""

    def __init__(self, name="", year=0, cost=0):
        """Initialise guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation of guitar"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Get the age of the guitar from the current year"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return True if the age of the guitar is greater than 50 years"""
        return self.get_age() > VINTAGE_AGE

    def __lt__(self, other):
        """Sort Guitars by year released."""
        return self.year < other.year
