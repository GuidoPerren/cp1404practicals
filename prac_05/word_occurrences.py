"""
Word Occurrences
Estimate: 10 minutes
Actual:   xx minutes
"""

def main():
    word_dict = {}
    sentence = (input("Enter short state: ")).lower()
    for word in sentence.split():
        if word_dict.get(word):
            word_dict[word] = word_dict[word] + 1
        else:
            word_dict[word] = 1

    print(word_dict)

main()