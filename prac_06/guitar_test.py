from guitar import Guitar

def main():
    # test_guitar = Guitar(name="Fancy Pants", year=1965, cost=1700.40)
    # print(test_guitar)

    guitar_list = []
    guitar_list.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitar_list.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    guitar_list.append(Guitar("Fancy Pants", 1965, 1700.40))

    for i, guitar in enumerate(guitar_list, 1):
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{guitar.vintage_string}")

main()