import random

SMALLEST_NUMBER = 1
LARGEST_NUMBER = 45
AMOUNT_OF_NUMBERS_PER_LINE = 6


def main():
    try:
        quick_pick_amount = int(input("How many quick picks? "))
        for i in range(0, quick_pick_amount):
            random_number_list = generate_unique_randoms(
                SMALLEST_NUMBER, LARGEST_NUMBER, AMOUNT_OF_NUMBERS_PER_LINE)
            random_number_list = sorted(random_number_list)
            print(" ".join(f"{number:2}" for number in random_number_list))
            # print_formatted_random_numbers(random_number_list, (len(str(LARGEST_NUMBER)) + 1) )

    except ValueError:
        print("Please enter an integer")


def generate_unique_randoms(smallest, largest, amount):
    random_numbers = []
    while len(random_numbers) != amount:
        random_number_to_add = random.randint(smallest, largest)
        if random_number_to_add not in random_numbers:
            random_numbers.append(random_number_to_add)

    return random_numbers


def print_formatted_random_numbers(random_number_list, width):
    print_string = f""
    for number in random_number_list:
        print_string += f"{number:{width}}"

    print(print_string)


main()
