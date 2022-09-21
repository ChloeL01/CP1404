"""
CP1404/CP5632 - Password stars
"""


def main():
    """Get and print a password"""
    password = get_password()
    print_password(password)


def print_password(password):
    """Print the number of *'s for the password length"""
    for i in range(len(password)):
        print("*", end="")


def get_password():
    """Check for a valid password"""
    password = input("Password: ")
    while len(password) < 8:
        print("Invalid, must be at least 8 characters")
        password = input("Password: ")
    return password


main()
