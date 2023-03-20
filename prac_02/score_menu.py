import random

def grade_score(score):

    grade_text = ""

    if score < 0 or score > 100:
        grade_text = ("Invalid score")
    else:
        if score >= 90:
            grade_text = ("Excellent")
        elif score >= 50:
            grade_text = ("Passable")
        elif score < 50:
            grade_text = ("Bad")

    return  grade_text

def get_random_score():
    random_score = random.randrange(0, 101, 1)
    return random_score

def print_asterisks(score):
    print(score * "*")

def main():
    print('(G)et a valid score (must be 0-100 inclusive)\n(P)rint result\n(S)how stars\n(Q)uit')
    choice = str(input())
    choice = choice.upper()
    score = 0
    while choice != 'Q':
        if choice == 'G':
            score = get_random_score()
            print(f"Your score is: {score}")
        elif choice == 'P':
            grade = grade_score(score)
            print(grade)
        elif choice == 'S':
            print_asterisks(score)
        else:
            print("Invalid choice")

        print()
        print('(G)et a valid score (must be 0-100 inclusive)\n(P)rint result\n(S)how stars\n(Q)uit')
        choice = str(input())

    print("Farewell")

main()