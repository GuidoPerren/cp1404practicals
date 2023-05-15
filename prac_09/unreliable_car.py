from prac_09.car import Car
from random import uniform


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        self.name = name
        self.fuel = fuel
        if reliability > 100.0:
            reliability = 100.0
        elif reliability < 0.0:
            reliability = 0.0
        self.reliability = reliability
        self.odometer = 0

    def drive(self, distance):
        if uniform(0, 100) < self.reliability:
            if distance > self.fuel:
                distance = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
            self.odometer += distance
        else:
            distance = 0
        return distance
