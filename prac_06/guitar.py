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

