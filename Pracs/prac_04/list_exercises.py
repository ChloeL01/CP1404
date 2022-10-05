"""
CP1404/CP5632 - List warmup - Chloe Laing

output vvv

Number: 5
   Number: 20
   Number: 1
   Number: 2
   Number: 3
   The first number is 5
   The last number is 3
   The smallest number is 1
   The largest number is 20
   The average of the numbers is 6.2

"""

NUMBER = 5

numbers = []
number = int(input("Number: "))
numbers.append(number)
for i in range(NUMBER - 1):
    number = int(input("Number: "))
    numbers.append(number)
# print(numbers)
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers)/NUMBER}")

# Woefully inadequate security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
user_username = input("Username: ")
if user_username in usernames:
    print("Access granted")
else:
    print("Access denied")
