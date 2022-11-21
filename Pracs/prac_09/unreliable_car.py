"""Prac 09 - Unreliable car"""
import random

from Pracs.prac_09.car import Car


class UnreliableCar(Car):
    """Unreliable car."""

    def __init__(self, name, fuel, reliability):
        """Initialise."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_number = random.randint(0, 100)
        if random_number < self.reliability:
            if distance > self.fuel:
                distance = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
            self.odometer += distance
            # print(random_number)  # testing
            return distance
        return 0
