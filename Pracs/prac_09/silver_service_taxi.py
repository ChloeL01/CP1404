"""Prac 09 - Silver service taxi class"""
from Pracs.prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Silver service taxi class."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise s silver service taxi object."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = self.price_per_km * self.fanciness

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return string representation."""
        return f"{super().__str__()}, plus flagfall of ${self.flagfall:.2f}"
