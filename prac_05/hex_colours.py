import re

import requests


# function has to be defined up here, otherwise it cannot be used to define COLOR_DICT
def get_colors_from_website():
    return_dictionary = {}
    r = requests.get(WEBSITE_URL)
    matches = re.findall('<tr><td>([\w\d\w\s]+)<\/td><td.style="background-color:(#[\w\d]+)', str(r.content))
    for match in matches:
        return_dictionary[(match[0]).lower()] = (match[1]).lower()

    return return_dictionary


WEBSITE_URL = "https://www.color-hex.com/color-names.html"
COLOR_DICT = get_colors_from_website()


def main():
    color_name = (input("Enter color Name: ")).lower()
    while color_name != "":
        try:
            color_code = COLOR_DICT.get(color_name)
            print(f"{color_name} is {color_code}")
        except:
            print(f"{color_name} was not found in the dictionary")
        color_name = (input("Enter color Name: ")).lower()


main()
