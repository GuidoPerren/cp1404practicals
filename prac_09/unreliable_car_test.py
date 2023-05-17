from unreliable_car import UnreliableCar

def main():
    name = "uc01"
    fuel = 100
    reliability = 50.5
    my_uc = UnreliableCar(name, fuel, reliability)
    distance_driven = my_uc.drive(10)

    if distance_driven == 0:
        print("card didnt start")
    else:
        print(f"car drove {distance_driven}km")

if __name__ == '__main__':
    main()