def main():
    # Read the guitars from the file and store them in a list
    guitars = []
    with open('guitars.csv', 'r') as file:
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

class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = int(year)
        self.cost = float(cost)

    def __lt__(self, other):
        return self.year < other.year

if __name__ == '__main__':
    main()