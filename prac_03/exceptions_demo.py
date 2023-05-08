"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
It will occur when the user input for numerator or donominator is NOT an Integer

2. When will a ZeroDivisionError occur?
This will occur when the user inputs a 0 for the denominator and the program tries to devide by 0

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
checking if the denomintaor is 0

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if(denominator > 0):
        fraction = numerator / denominator
        print(fraction)
    else:
        print("Denominator can not be 0")
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")