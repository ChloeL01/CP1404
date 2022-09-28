"""
CP1404/CP5632 - Files
"""

# 1
name = input("Name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# 2
in_file = open("name.txt", "r")
print(f"Your name is {in_file.readline()}")

# 3
numbers = [17, 42, 400]
out_file = open("numbers.txt", "w")
for number in numbers:
    print(number, file=out_file)
out_file.close()

in_file = open("numbers.txt", "r")
number_1 = int(in_file.readline())
number_2 = int(in_file.readline())
print(number_1 + number_2)
in_file.close()

# 4
total = 0
in_file = open("numbers.txt", "r")
for line in in_file:
    total += int(line)
print(total)
in_file.close()
