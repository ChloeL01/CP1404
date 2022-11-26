"""Prac 09 - Unreliable car test"""
from Pracs.prac_09.unreliable_car import UnreliableCar

my_unreliable_car = UnreliableCar("This car", 60, 50)
distance = my_unreliable_car.drive(20)
print(f"Distance driven: {distance}kms. Fuel: {my_unreliable_car.fuel}L")
