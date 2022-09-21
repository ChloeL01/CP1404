"""Password stars"""
password = input("Password: ")
while len(password) < 8:
    print("Invalid, must be at least 8 characters")
    password = input("Password: ")
for i in range(len(password)):
    print("*", end="")
