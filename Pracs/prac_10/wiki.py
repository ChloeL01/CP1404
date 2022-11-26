"""Week 10 - wiki"""

import wikipedia


def main():
    """Search wikipedia and return results."""
    user_input = input("Enter page title or search phrase: ")
    while user_input != "":
        try:
            page = wikipedia.page(user_input)
            print(f"Page title: {page.title}, url: {page.url}")
            print(page.summary)
        except wikipedia.exceptions.DisambiguationError as error:
            print("Page does not exits, see below for options:")
            print(error.options)
        user_input = input("Enter page title or search phrase: ")
    print("Thanks for searching :)")


main()
