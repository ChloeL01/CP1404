"""Prac 09 - silver service test"""
from Pracs.prac_09.silver_service_taxi import SilverService

hummer = SilverService("Hummer", 200, 4)
print(hummer)

silver_service_taxi = SilverService("Silver service", 100, 2)
silver_service_taxi.drive(18)
fare = silver_service_taxi.get_fare()
print(silver_service_taxi)
print(f"total fare ${fare}")
