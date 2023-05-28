import wikipedia

def main():
    while True:
        search_input = input("Enter a page title or search phrase (or press Enter to quit): ")
        if not search_input:
            break

        try:
            page = wikipedia.page(search_input, auto_suggest=True)
            print("Title:", page.title)
            print("Summary:", page.summary)
            print("URL:", page.url)
        except wikipedia.exceptions.DisambiguationError as e:
            print("Disambiguation Error: Please specify your search phrase more precisely.")
        except wikipedia.exceptions.PageError as e:
            print("Page Error: The page does not exist.")

        print()


if __name__ == '__main__':
    main()