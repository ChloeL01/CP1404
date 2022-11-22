"""Prac 09 - taxi simulator"""
from Pracs.prac_09.silver_service_taxi import SilverServiceTaxi
from Pracs.prac_09.taxi import Taxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """..."""
    print("Let's drive!")
    print(MENU)
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_cost = 0.0
    cost = 0.0
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print_taxi(taxis)
            current_taxi = choose_taxi(taxis)
        elif choice == "d":
            cost = drive_taxi(current_taxi)
            total_cost += cost
        else:
            print("Invalid option")

        print(f"Bill to date ${total_cost}")
        print(MENU)
        choice = input(">>> ")
    print(f"Total trip cost: ${total_cost}")
    print("Taxis are now: ")
    print(print_taxi(taxis))


def print_taxi(taxis):
    """Print the taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxi):
    """Choose a taxi."""
    choice = int(input("Choose taxi: "))
    if choice > len(taxi) and choice < 0:
        print("Invalid taxi choice")
    else:
        # print(taxi[choice]) test
        return taxi[choice]


def drive_taxi(taxi):
    """Drive the taxi."""
    if taxi is not None:
        taxi.start_fare()
        distance = float(input("Drive how far? "))
        taxi.drive(distance)
        cost = taxi.get_fare()
        print(f"Your {taxi.name} trip cost you ${cost}")
        return cost
    else:
        print("You need to choose a taxi before you can drive")
        return 0.0


if __name__ == '__main__':
    main()
