"""
Word Occurrences
Estimate: 20 minutes
Actual:   32 minutes
"""

FILENAME = "wimbledon.csv"
WIDTH_CORRECTION = 1

def main():
    wimbledon_list = get_wimbledon_data()
    champion_won_dict = {}
    for wimbledon in wimbledon_list:
        if wimbledon.year != "Year":
            if champion_won_dict.get(wimbledon.champion):
                champion_won_dict[wimbledon.champion] = champion_won_dict[wimbledon.champion] + 1
            else:
                champion_won_dict[wimbledon.champion] = 1

    #Task 1
    print("Wimbledon Champions: ")

    champion_country_list = []
    longest_champion_name = len(max(champion_won_dict.keys(), key=len)) + WIDTH_CORRECTION
    for champion in dict(sorted(champion_won_dict.items(), key=lambda item: item[1], reverse=True)):
        print(f"{champion:{longest_champion_name}}: {champion_won_dict[champion]}")
        champion_country_list.append((next((wimbledon for wimbledon in wimbledon_list if wimbledon.champion == champion), None)).country_champion)

    #Task 2
    print_string = " ".join(sorted(set(champion_country_list)))
    print(f"These {len(set(champion_country_list))} countries have won Wimbledon: ")
    print(print_string)




class Wimbledon:
    def __init__(self, year, country_champion, champion, country_runner_up, runner_up, score):
        self.year = year
        self.country_champion = country_champion
        self.champion = champion
        self.country_runner_up = country_runner_up
        self.runner_up = runner_up
        self.score = score


def get_wimbledon_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    wimbledon_list = []
    with open(FILENAME, "r", encoding="utf-8-sig") as input_file:
        for line in input_file:
            line = line.strip()  # Remove the \n
            parts = line.split(',')  # Separate the data into its parts
            wimbledon_to_add = Wimbledon(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5])
            wimbledon_list.append(wimbledon_to_add)
    return wimbledon_list


main()
