from guitar import Guitar

"""
requested input should look like:


My guitars!
Name: Fender Stratocaster
Year: 2014
Cost: $765.4
Fender Stratocaster (2014) : $765.40 added.

"""

def main():
    print('My Guitars')
    continue_to_run = True
    guitars = []

    while continue_to_run:
        name = str(input("Name: "))
        if name:
            try:
                year = int(input("Year: "))
                cost = float(input("Cost: "))
                guitars.append(Guitar(name, year, cost))
                print(f"{name} ({year}) : ${cost} added.")
                print()

            except ValueError:
                print("The values year and cost need to be numerical")
                print()
        else:
            continue_to_run = False

    if guitars:
        for i, guitar in enumerate(guitars, 1):
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{guitar.vintage_string}")


main()