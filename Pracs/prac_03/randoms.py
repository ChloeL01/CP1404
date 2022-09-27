"""
CP1404/CP5632 - Randoms



What did you see on line 1?
    What was the smallest number you could have seen, what was the largest?
    - the smallest number is 5 and the largest is 20 because they are the limits.

What did you see on line 2?
    What was the smallest number you could have seen, what was the largest?
    - the smallest number is 3 and the largest is 9 because it starts at 3 and increases by 2 up till 9.

    Could line 2 have produced a 4?
    - no because it starts at 3 and goes up in increments of 2, meaning the next one would be a 5, skipping 4.

What did you see on line 3?
    What was the smallest number you could have seen, what was the largest?
    - the smallest number is 2.500... and the largest is 5.500... because they are the limits.

Write code, not a comment, to produce a random number between 1 and 100 inclusive
"""
import random
print(random.randint(1, 100))
