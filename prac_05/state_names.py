"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}

def main():
    for line in CODE_TO_NAME:
        print(f"{line:3} is {CODE_TO_NAME[line]}")

    state_code = (input("Enter short state: ")).upper()
    while state_code != "":
        try:
            print(state_code, "is", CODE_TO_NAME[state_code])
        except:
            print("Invalid short state")
        state_code = input("Enter short state: ")


main()