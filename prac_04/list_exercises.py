
def main():
    number_list = []

    for i in range(0, 5):
        user_input = int(input("Number: "))
        number_list.append(user_input)

    print(number_list[0])
    print(number_list[-1])
    print(min(number_list))
    print(max(number_list))
    print((sum(number_list) / len(number_list)))



main()