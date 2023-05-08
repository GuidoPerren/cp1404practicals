"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
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




def main():
    """
    main program
    """

    #Part 1
    #score = float(input("Enter score: "))
    #grade_text = grade_score(score)
    #print(grade_text)

    #Part 2
    random_score = random.randrange(0, 101, 1)
    grade_text = grade_score(random_score)
    print(f"The score {random_score} is an {grade_text} grade")

main()