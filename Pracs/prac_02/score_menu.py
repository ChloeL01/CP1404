"""
CP1404 - Score Menu
"""
MENU = """(G)et score
(P)rint score
(S)how lines
(Q)uit"""


def main():
    score = 0
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(f"{score} is {return_score_result(score)}")
        elif choice == "S":
            print_line(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()


def print_line(score):
    print("*" * score)


def get_valid_score():
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid Score: ")
        score = int(input("Score: "))
    return score


def return_score_result(score):
    if score < 0 or score > 100:
        return "Invalid score, try again!"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
