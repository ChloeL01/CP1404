"""Guitar class"""


class Guitar:
    """Guitar class"""

    def __init__(self, name="", year=0, cost=0):
        """Initialise guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation of guitar"""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """Get the age of the guitar from the current year"""
        return 2022 - self.year

    def is_vintage(self):
        """Return True if the age of the guitar is greater than 50 years"""
        return self.get_age() > 50

