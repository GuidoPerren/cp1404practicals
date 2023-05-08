import random
#Write 3 different versions of code to generate a random Boolean (True or False).

result_1 = random.randint(1,2)
if result_1 == 1:
    print(True)
else:
    print(False)

list_of_possible_results = [True, False]

#Version 1
random.shuffle(list_of_possible_results)
print(list_of_possible_results[0])

#Version 2
choice = random.choice(list_of_possible_results)
print(choice)
