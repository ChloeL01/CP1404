"""
CP1404/CP5632 wimbledon

"""
FILENAME = "../../data/wimbledon.csv"


def main():
    """Read data and print winners and winning countries."""
    data = get_data(FILENAME)
    winner_to_wins, countries = process_data(data)
    display_data(winner_to_wins, countries)


def get_data(file_name):
    """Read data from file formatted like: Year,Country,Champion,Country,Runner-up,Score in the final"""
    data = []
    with open(file_name, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            parts = line.strip().split(",")  # separate the data into parts
            data.append(parts)
    data.pop(0)  # remove the header, 'Year,Country,Champion,Country,Runner-up,Score in the final' from the list
    return data


def process_data(data):
    """Create a set of countries and a dictionary of winner."""
    winner_to_wins = {}
    countries = set()
    for lines in data:
        countries.add(lines[1])     # adds countries to a list which is from the data at index 1
        winner_to_wins[lines[2]] = winner_to_wins.get(lines[2], 0) + 1  # counts the amount of times someone has won
    return winner_to_wins, countries


def display_data(winner_to_wins, countries):
    """Display the winner and winning countries"""
    print("Wimbledon Champions:")
    for winner, wins in winner_to_wins.items():
        print(winner, wins)

    print(f"These {len(countries)} countries have won Wimbledon")
    winning_countries = ", ".join(country for country in sorted(countries))
    print(winning_countries)


main()
