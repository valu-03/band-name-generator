import generator


def ask_genre():
    print("Available genres:")
    for genre in generator.GENRES:
        print(f" - {genre}")
    answer = input("Genre? ").strip().lower()
    if answer in generator.GENRES:
        return answer
    print("Unknown genre — using metal.")
    return "metal"


def ask_how_many():
    answer = input("How many names? ")
    try:
        return int(answer)
    except ValueError:
        print("That's not a number — using 5.")
        return 5


def save_from_list(names):
    if not names:
        print("Generate some names first.")
        return
    answer = input("Which number? ").strip()
    try:
        index = int(answer) - 1
    except ValueError:
        print("That's not a number.")
        return
    if index < 0 or index >= len(names):
        print("There's no name with that number.")
        return
    name = names[index]
    if generator.save_favorite(name):
        print(f"Saved: {name}")
    else:
        print(f"{name} is already in your favourites.")


def show_favorites():
    favorites = generator.load_favorites()
    if not favorites:
        print("No favourites yet.")
        return
    print("Your favourites:")
    for number, name in enumerate(favorites, start=1):
        print(f"{number}. {name}")


def main():
    last_names = []
    while True:
        print()
        print("1) Generate names")
        print("2) Save one of them")
        print("3) Show favourites")
        print("4) Quit")
        choice = input("> ").strip()

        if choice == "1":
            last_names = generator.generate_many(ask_genre(), ask_how_many())
            for number, name in enumerate(last_names, start=1):
                print(f"{number}. {name}")
        elif choice == "2":
            save_from_list(last_names)
        elif choice == "3":
            show_favorites()
        elif choice == "4":
            print("Bye.")
            break
        else:
            print("Unknown option — type 1 to 4.")


if __name__ == "__main__":
    main()