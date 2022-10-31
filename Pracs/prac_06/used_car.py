"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""
from Pracs.prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    # demo code
    # my_car = Car(180)
    # my_car.drive(30)
    # print(f"Car has fuel: {my_car.fuel}")
    # print(my_car)

    # part 1-5
    # limo = Car(100)
    # limo.add_fuel(20)
    # print(f"limo has fuel: {limo.fuel}")
    # limo.drive(115)
    # print(limo)

    # part 6-7 (added a name field)
    limo = Car(100, "limo")
    limo.add_fuel(20)
    print(f"{limo.name} has fuel: {limo.fuel}")
    limo.drive(115)
    print(limo)


main()
