from taxi import Taxi


class SilverServiceTaxi(Taxi):

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return f"{super().__str__()} plus flagfall of ${SilverServiceTaxi.flagfall}"

    def get_fare(self):
        return super().get_fare() + SilverServiceTaxi.flagfall
