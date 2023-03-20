#Example
for i in range(1, 21, 2):
    print(i, end=' ')
print()

#Exercise A:
for i in range(0, 101, 10):
    print(i, end=' ')
print()

#Exercise B:
for i in range(20, 0, -1):
    print(i, end=' ')
print()

#Exercise C:
number_of_stars = int(input('Number of stars: '))
while number_of_stars > 0:
    stars = ""
    for i in range(0, number_of_stars):
        stars += "*"
    print(stars)
    number_of_stars = int(input('Number of stars: '))

#Exercise C:
number_of_stars = int(input('Number of stars: '))
while number_of_stars > 0:
    stars = ""
    for i in range(0, number_of_stars):
        stars += "*"
        print(stars)
    number_of_stars = int(input('Number of stars: '))