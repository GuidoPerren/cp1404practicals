numbers = [3, 1, 4, 1, 5, 9, 2]

#Questions
"""
numbers[0]
A: Will return the number from the list with the index 0 = 3

numbers[-1]
A: Will return the last number from list with the highest index = 2

numbers[3]
A: Will return the number from the list at index 3 = 1

numbers[:-1]
A: Will return every entry from the list until the last (-1) entry = [3,1,4,1,5,9]

numbers[3:4]
A: Will return all values starting from the third entry and ending before the fourth entry = [1]

5 in numbers
A: This will check if the number 5 is within the list; which it is = true

7 in numbers
A: This will check if the number 5 is within the list; which it is NOT = false

"3" in numbers
A: This will check if the STRING 3 is within the list; which it is NOT = false

numbers + [6, 5, 3]
A: This will add the numbers 6, 5 and 3 to the list and print it, since there is no equal sign it will
not override the existing numbers variable, resulting in the output = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
"""