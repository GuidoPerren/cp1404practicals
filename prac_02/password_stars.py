# CONSTANTS
MINIMUM_PASSWORD_LENGTH = 12


def main():
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    print(len(password) * "*")


def get_password():
    password_input = str(input("Password: "))
    while len(password_input) < MINIMUM_PASSWORD_LENGTH:
        print(f"Please enter a password of at least {MINIMUM_PASSWORD_LENGTH} charactes")
        password_input = str(input("Password: "))
    return password_input


main()