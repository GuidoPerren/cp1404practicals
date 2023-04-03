"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    class_info_list = get_data()
    print_class_informations(class_info_list)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    list_of_parts = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        list_of_parts.append(parts)
    input_file.close()
    return list_of_parts

def print_class_informations(class_info_list):
    for line in class_info_list:
        print(f"{line[0]} is taught by {line[1]} and has {line[2]} students")


main()