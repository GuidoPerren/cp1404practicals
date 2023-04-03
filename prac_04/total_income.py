"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    months = int(input("How many months? "))

    for number_of_months in range(1, months + 1):
        income = float(input(f"Enter income for month {number_of_months}: "))
        incomes.append(income)

    print("\nIncome Report\n-------------")
    print_income_report(incomes)


def print_income_report(incomes):
    total = 0
    #for number_of_months in range(1, len(incomes) + 1):
        #income = incomes[number_of_months - 1]
        #total += income
        #print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(number_of_months, income, total))

    #Version from Practice - Output from former print got commented
    for income in enumerate(incomes):
        total += income[1]
        print(f"Month {(1 + income[0]):2} - Income: ${income[1]:10.2f} Total: ${total:10.2f}")


main()