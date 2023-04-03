
def main():
    number_list = []
    username_list = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']

    username_input = str(input("Username: "))
    if(username_input in username_list):

        print("Access granted")

        for i in range(0, 5):
            user_input = int(input("Number: "))
            number_list.append(user_input)

        print(number_list[0])
        print(number_list[-1])
        print(min(number_list))
        print(max(number_list))
        print((sum(number_list) / len(number_list)))
    else:
        print("Access denied")



main()