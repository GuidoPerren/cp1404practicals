"""
Word Occurrences
Estimate: 15 minutes
Actual:   11 minutes
"""

def main():
    mail_and_name_dict = {}

    email_address = (input("Email: ")).lower()
    while email_address != "":
        name_separated_by_dot = email_address.split("@")[0]
        name_separated_by_space = " ".join(name.capitalize() for name in name_separated_by_dot.split("."))
        user_choice = (input(f"Is your name {name_separated_by_space}? (Y/n)")).lower()
        if user_choice == "" or user_choice == "y":
            mail_and_name_dict[email_address] = name_separated_by_space
        else:
            name_manually = input(f"Name: ")
            mail_and_name_dict[email_address] = name_manually
        email_address = (input("Email: ")).lower()

    for key in mail_and_name_dict:
        print(f"{mail_and_name_dict[key]} ({key})")


main()