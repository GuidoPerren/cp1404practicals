from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]


    print("Let's drive!")
    print("(q)uit, (c)hoose taxi, (d)rive)")
    user_choice = str(input()).upper()

    selected_taxi_index = -1
    bill_to_date = 0.0
    while user_choice != 'Q':
        if user_choice == 'C':
            print("Taxis available:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            try:
                taxi_choice = int(input("Choose taxi: "))
                if 0 <= taxi_choice < len(taxis):
                    selected_taxi_index = taxi_choice
            except ValueError:
                print("Please refer to the numbers at the beginning of each taxi")
        if user_choice == 'D':
            if selected_taxi_index >= 0:
                try:
                    distance_to_drive = int(input("Drive how far? "))
                    taxis[selected_taxi_index].start_fare()
                    taxis[selected_taxi_index].drive(distance_to_drive)
                    trip_cost = taxis[selected_taxi_index].get_fare()
                    bill_to_date += trip_cost
                    print(f"Your {taxis[selected_taxi_index].name} trip cost you ${trip_cost:.2f}")
                except ValueError:
                    print("Please enter a valid distance and round it up to the next number.")
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")

        print(f"Bill to date: ${bill_to_date:.2f}")
        print("(q)uit, (c)hoose taxi, (d)rive)")
        user_choice = str(input()).upper()



if __name__ == '__main__':
    main()
