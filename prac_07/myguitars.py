from guitar import Guitar

PATH_TO_CSV = "guitars.csv"
def main():
    # Read the guitars from the file and store them in a list
    guitars = []
    with open(PATH_TO_CSV, 'r') as file:
        for line in file:
            name, year, cost = line.strip().split(',')
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)

    # Display guitars using a loop
    for guitar in guitars:
        print(guitar.name, guitar.year, guitar.cost)

    # Sort the list by year (oldest to newest) and display them in sorted order
    guitars.sort()
    print("\nSorted by year:")
    for guitar in guitars:
        print(guitar.name, guitar.year, guitar.cost)

    continue_to_run = True
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
            with open(PATH_TO_CSV, 'w') as file:
                for guitar in guitars:
                    file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")

main()