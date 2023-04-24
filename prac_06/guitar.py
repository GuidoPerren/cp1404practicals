"""
Expected: 1.75h
Was: 1.25h
"""
import datetime


class Guitar():

    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost
        self.vintage_string = " (vintage)" if (datetime.date.today().year - year) >= 40 else ""

    def __str__(self):
        return f"{self.name} ({self.year}), worth ${self.cost}{self.vintage_string}"


# test_guitar = Guitar(name="Fancy Pants", year=1965, cost=1700.40)
# print(test_guitar)

guitar_list = []
guitar_list.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitar_list.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
guitar_list.append(Guitar("Fancy Pants", 1965, 1700.40))

i = 1
for guitar in guitar_list:
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{guitar.vintage_string}")
    i += 1
