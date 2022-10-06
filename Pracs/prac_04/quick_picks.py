"""
CP1404/CP5632 - Quick picks - Chloe Laing
"""

import random
MIN = 1
MAX = 45
NUMBER_OF_LINES = 6

number_of_quick_pick = int(input("How many quick picks? "))

for column in range(number_of_quick_pick):
    quick_pick = []
    for line in range(NUMBER_OF_LINES):
        number = random.randint(MIN, MAX)
        # if the number is in the list then get a new number
        while number in quick_pick:
            number = random.randint(MIN, MAX)
        quick_pick.append(number)
    quick_pick.sort()
    # arrange the numbers nicely
    print(" ".join(f"{number:2}" for number in quick_pick))
