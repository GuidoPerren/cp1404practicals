def main():
    number_list = []

    username_input = str(input("Username: "))
    if check_username(username_input):

        print("Access granted")

        user_input = int(input("Number 1: "))
        while user_input > 0:
            number_list.append(user_input)
            user_input = int(input(f"Number {(len(number_list) + 1)}: "))

        print(number_list[0])
        print(number_list[-1])
        print(min(number_list))
        print(max(number_list))
        print((sum(number_list) / len(number_list)))
    else:
        print("Access denied")


def check_username(username):
    username_list = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                     'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                     'bob']

    return (username in username_list)


main()
