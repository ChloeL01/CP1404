"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        # income = float(input("Enter income for month " + str(month) + ": "))
        incomes.append(income)

    print_report(incomes, number_of_months)


def print_report(incomes, number_of_months):
    """Print the report nicely."""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, number_of_months + 1):
        income = calculate_income(incomes, month)
        total = total + income
        print("Month {:2} - Income: ${:10.2f}       Total: ${:10.2f}".format(month, income, total))


def calculate_income(incomes, month):
    """Calculate the income."""
    income = incomes[month - 1]
    return income


main()
