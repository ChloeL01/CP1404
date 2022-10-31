"""
CP1404/CP5632 programming languages class

"""


class ProgrammingLanguage:
    """ Programming class"""

    def __init__(self, name="", typing=False, reflection=False, year=0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing == "Dynamic"

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflections={self.reflection}, First appeared in {self.year}"
