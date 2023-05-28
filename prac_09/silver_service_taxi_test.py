from silver_service_taxi import SilverServiceTaxi

def main():
    name = "sst01"
    fuel = 100
    my_silver_service_taxi = SilverServiceTaxi(name, fuel, 2)
    my_silver_service_taxi.drive(18)
    print(my_silver_service_taxi.get_fare())
    print(my_silver_service_taxi)


if __name__ == '__main__':
    main()