"""
CP1404/CP5632 - program to determine score status
"""
import random


def main():
    """Get a score then print"""
    score = int(input("Enter score: "))
    print(return_score_result(score))
    # get a random number between 0 and 100
    score = random.randint(0, 100)
    print(f"{score} is {return_score_result(score)}")


def return_score_result(score):
    """Return the score result"""
    if score < 0 or score > 100:
        return "Invalid score, try again!"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
