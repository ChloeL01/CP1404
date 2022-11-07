"""CP1404/CP5632 Project class"""
import datetime

COMPLETION_PERCENTAGE = 100


class Project:
    """Represent a project object."""

    def __init__(self, name, start_date, priority, cost, completion_percentage):
        """Initialise a Project."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost = cost
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a string representation."""
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, " \
               f"estimate: ${self.cost:,.2f}, completion: {self.completion_percentage}%"

    def is_complete(self):
        """Return True if percentage is less than 100% complete."""
        return self.completion_percentage < COMPLETION_PERCENTAGE

    def __getitem__(self, item):
        """Get item from index."""
        return item

    def __lt__(self, other):
        """Sort Projects by priority."""
        return self.priority < other.priority
