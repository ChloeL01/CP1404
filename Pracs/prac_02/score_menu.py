"""
CP1404 - Score Menu
"""

MENU = """(G)et score
(P)rint score
(S)how lines
(Q)uit"""


def main():
    """Main menu"""
    score = 0
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":   # get a valid score
            score = get_valid_score()
        elif choice == "P":  # print the score
            print(f"{score} is {return_score_result(score)}")
        elif choice == "S":  # print *'s for the length of the score
            print_line(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell")   # quit message


def print_line(score):
    """Print a line of *'s for the score's length"""
    print("*" * score)


def get_valid_score():
    """Get a valid score"""
    score = int(input("Score: "))
    # score must be between 0 and 100
    while score < 0 or score > 100:
        print("Invalid Score: ")
        score = int(input("Score: "))
    return score


def return_score_result(score):
    """Return the score's result"""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
