"""Prac 09 - band class"""


class Band:
    """Band class"""

    def __init__(self, band_name):
        """Initialise a band object."""
        self.band_name = band_name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a band."""
        return f"{self.band_name} ({','.join([str(musician) for musician in self.musicians])})"

    def __repr__(self):
        """Return a string representation of a band, showing variables."""
        return str(self)

    def add(self, musician_name):
        """Add a musician to the band."""
        self.musicians.append(musician_name)

    def play(self):
        """Return a string showing the musician playing their instrument"""
        for musician in self.musicians:
            print(f"{musician.play()} ")
