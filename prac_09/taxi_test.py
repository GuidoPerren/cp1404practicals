from taxi import Taxi

def main():
    taxi_name = "Prius 1"
    taxi_fuel = 100
    taxi_price_per_km = 1.23

    my_taxi = Taxi(name=taxi_name, fuel=taxi_fuel)

    my_taxi.drive(40)
    print(my_taxi.get_fare())
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi.get_fare())

if __name__ == '__main__':
    main()