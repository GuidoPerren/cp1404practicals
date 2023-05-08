#input X and Y
input_x = int(input("Number X: "))
input_y = int(input("Number Y: "))

print("Show the (E)ven numbers from x to y")
print("Show the (O)dd numbers from x to y")
print("Show the (S)quares from x to y")
print("(Q)uit the program")
choice = str(input())

while choice != 'Q':
    if choice == 'E':
        for i in range(input_x, (input_y + 1)):
            if (i % 2) == 0:
                print(i, end=' ')

    if choice == 'O':
        for i in range(input_x, (input_y + 1)):
            if (i % 2) == 1:
                print(i, end=' ')

    if choice == 'S':
        for i in range(input_x, (input_y + 1)):
            print((i*i), end=' ')

    #Creates two new lines for better readability
    print("\n\n")
    print("Show the (E)ven numbers from x to y")
    print("Show the (O)dd numbers from x to y")
    print("Show the (S)quares from x to y")
    print("(Q)uit the program")
    choice = str(input())