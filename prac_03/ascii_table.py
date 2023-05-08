MIN_NUMBER = 33
MAX_NUMBER = 127

def main():
    char_input = str(input("Enter a character: "))
    print(f"The ASCII code for {char_input} is {ord(char_input)}")

    try:
        number_input = int(input(f"Enter a number between {MIN_NUMBER} and {MAX_NUMBER}: "))
        if(MIN_NUMBER <= number_input <= MAX_NUMBER):
            print(f"The character for {number_input} is {chr(number_input)}")
        else:
            print("Number is outside the range")
    except ValueError:
        print("Please Enter a valid Integer")

    for i in range(MIN_NUMBER, (MAX_NUMBER + 1)):
        print(f"{i} {chr(i)}")

main()