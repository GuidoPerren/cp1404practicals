# altered function from prac_02 - more_scores.py
def write_text_file(path, text):
    with open(path, 'w') as file:
        file.write(text)
        file.write('\n')
        file.close()


def get_text_file_content(path):
    with open(path, 'r') as file:
        lines_read = file.readlines()
        return lines_read


FILE_NAME_EXCERSISE_1 = "names.txt"
FILE_NAME_EXCERSISE_2 = "numbers.txt"

# Write to File
name_of_user = str(input("Enter your name: "))
write_text_file(FILE_NAME_EXCERSISE_1, name_of_user)

# Read File
lines_read = get_text_file_content(FILE_NAME_EXCERSISE_1)
print(f"Your name is {lines_read[0]}")  # the name is stored in the first line, hence [0]

