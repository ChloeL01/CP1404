"""
CP1404/CP5632 emails

"""


def main():
    """Get email and name from user."""
    email_to_name = {}
    email_address = input("Email: ")

    while email_address != "":  # keeps going until a blank email is entered
        name = extract_name_from_email(email_address)
        answer = input(f"Is your name {name}? (Y/n) ").lower()

        if answer != "y" and answer != "":
            name = input("Name: ")
        email_to_name[email_address] = name
        email_address = input("Email: ")

    for email_address, name in email_to_name.items():
        print(f"{name} ({email_address})")


def extract_name_from_email(email):
    """Extract the name from the email address."""
    prefix = email.split('@')[0]    # split at the '@' symbol to get the name part
    name = prefix.split('.')        # separates the name if there's a '.' between first and last
    full_name = " ".join(name).title()  # join the first and last name together
    return full_name


main()
