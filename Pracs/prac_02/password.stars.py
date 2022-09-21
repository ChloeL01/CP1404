"""Password stars"""


def main():
    password = get_password()
    print_password(password)


def print_password(password):
    for i in range(len(password)):
        print("*", end="")


def get_password():
    password = input("Password: ")
    while len(password) < 8:
        print("Invalid, must be at least 8 characters")
        password = input("Password: ")
    return password


main()
