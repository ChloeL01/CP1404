"""
CP1404/CP5632 programming languages class

"""


class ProgrammingLanguage:
    """ Programming Language class"""

    def __init__(self, name="", typing=False, reflection=False, year=0):
        """Initialise a language instance"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True is language has dynamic typing"""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return string representation of language"""
        return f"{self.name}, {self.typing} Typing, Reflections={self.reflection}, First appeared in {self.year}"
