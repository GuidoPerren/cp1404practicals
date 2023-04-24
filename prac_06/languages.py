"""
Expected: 1h
Was: 50min
"""

from programming_language import ProgrammingLanguage

def main():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)


    print(python)

    programming_languages = [python, ruby, visual_basic]


main()