"""
Word Occurrences
Estimate: 10 minutes
Actual:   xx minutes
"""

WIDTH_CORRECTION = 1

def main():
    word_dict = {}
    sentence = (input("Enter short state: ")).lower()
    for word in sentence.split():
        if word_dict.get(word):
            word_dict[word] = word_dict[word] + 1
        else:
            word_dict[word] = 1

    longest_word_count = len(max(word_dict.keys(), key=len)) + WIDTH_CORRECTION
    for word in word_dict:
        print(f"{word:{longest_word_count}}: {word_dict[word]}")

main()