import random

GENRES = {
    "metal": {
        "adjectives": ["Blackened", "Eternal", "Savage", "Iron", "Frozen"],
        "nouns": ["Throne", "Serpents", "Ashes", "Storm", "Wolves"],
        "syllables": ["kor", "thak", "vor", "grim", "nax", "dur", "zul", "mor"],
    },
    "jazz": {
        "adjectives": ["Blue", "Midnight", "Velvet", "Smooth", "Wandering"],
        "nouns": ["Quartet", "Avenue", "Cats", "Rain", "Session"],
        "syllables": ["lu", "ma", "sa", "ri", "vo", "ne", "za", "do"],
    },
    "indie": {
        "adjectives": ["Tiny", "Paper", "Lonely", "Plastic", "Sunday"],
        "nouns": ["Bicycles", "Ghosts", "Postcards", "Summer", "Radio"],
        "syllables": ["mi", "lo", "ta", "ka", "sun", "el", "ry", "pa"],
    },
}


FAVORITES_FILE = "favorites.txt"


def load_favorites():
    try:
        with open(FAVORITES_FILE, "r", encoding="utf-8") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return []


def save_favorite(name):
    if name in load_favorites():
        return False
    with open(FAVORITES_FILE, "a", encoding="utf-8") as file:
        file.write(name + "\n")
    return True


def pattern_the_adjective_noun(words):
    adjective = random.choice(words["adjectives"])
    noun = random.choice(words["nouns"])
    return f"The {adjective} {noun}"


def pattern_noun_of_the_noun(words):
    first, second = random.sample(words["nouns"], 2)
    return f"{first} of the {second}"


def pattern_one_word(words):
    adjective = random.choice(words["adjectives"])
    noun = random.choice(words["nouns"])
    return adjective + noun.lower()


def pattern_invented(words):
    syllables = words["syllables"]
    length = random.randint(2, 3)
    name = ""
    for _ in range(length):
        name += random.choice(syllables)
    return name.capitalize()


patterns = [
    pattern_the_adjective_noun,
    pattern_noun_of_the_noun,
    pattern_one_word,
    pattern_invented,
]


def generate_name(genre):
    words = GENRES[genre]
    pattern = random.choice(patterns)
    return pattern(words)


def generate_many(genre, how_many):
    names = []
    attempts = 0
    while len(names) < how_many and attempts < how_many * 20:
        attempts += 1
        name = generate_name(genre)
        if name in names:
            continue
        names.append(name)
    return names
