"""Week 09 - Taxi test"""
from Pracs.prac_09.taxi import Taxi

my_taxi = Taxi("Primus 1", 100)
my_taxi.drive(40)
my_taxi.start_fare()
my_taxi.drive(100)
print(my_taxi)
print(f"current fare: ${my_taxi.get_fare()}")
