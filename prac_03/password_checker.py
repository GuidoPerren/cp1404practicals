"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

PRINT_CHAR_COUNT = False


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password):
    """Determine if the provided password is valid."""
    if not MIN_LENGTH <= len(password) <= MAX_LENGTH:
        return False

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if str.islower(char):
            count_lower+= 1
        if str.isupper(char):
            count_upper+= 1
        if str.isdigit(char):
            count_digit+= 1
        if char in SPECIAL_CHARACTERS:
            count_special += 1
        pass

    if PRINT_CHAR_COUNT:
        print(f"Lower characters: {count_lower}")
        print(f"Upper characters: {count_upper}")
        print(f"Digit characters: {count_digit}")
        print(f"Special characters: {count_special}")

    check_not_zero = count_lower * count_upper * count_digit
    if SPECIAL_CHARS_REQUIRED:
        check_not_zero = check_not_zero * count_special
    if check_not_zero > 0:
        return True
    else:
        return False


main()