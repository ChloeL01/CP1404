"""CP1404/CP5632 Project class"""
import datetime

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
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, " \
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

    def sort_by_date(self):
        """Sort by start date."""
        return self.start_date

    def compare_datetime(self, other_date):
        """Return True or False if date is equal to or larger than other date."""
        return self.start_date >= other_date
