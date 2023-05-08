import random

def append_text_file(path, text):
    with open(path, 'a') as file:
        file.write(text)
        file.write('\n')
        file.close()

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

def generate_n_scores(n):
    random_score_list = []
    for i in range(0, (n + 1)):
        random_score = random.randrange(0, 101, 1)
        random_score_list.append(random_score)
    return  random_score_list



def main():
    number_of_scores = int(input("Enter Number of scores to be generated: "))
    random_score_list = generate_n_scores(number_of_scores)
    for score in random_score_list:
        grade_text = grade_score(score)
        append_text_file("results.txt", f"{score} is {grade_text}")

main()