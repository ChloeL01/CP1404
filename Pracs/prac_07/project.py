"""CP1404/CP5632 Project class"""

COMPLETION_PERCENTAGE = 100


class Project:
    """Represent a project object."""

    def __init__(self, name, start_date, priority, cost, completion_percentage):
        """Initialise."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost = cost
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a string representation."""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost:,.2f}, " \
               f"completion: {self.completion_percentage}%"

    def is_complete(self):
        """Return True if percentage is less than 100% done."""
        return self.completion_percentage < COMPLETION_PERCENTAGE
