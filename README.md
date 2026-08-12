# Band Name Generator

A small Python project that invents band names, with two interfaces over one
engine: a terminal menu and a PyQt6 desktop window.

```
The Blackened Throne        ← "The <adjective> <noun>"
Serpents of the Ashes       ← "<noun> of the <noun>"
Frozenstorm                 ← fused single word
Grimvorzul                  ← invented from syllables
```

Names are genre-flavoured — metal, jazz and indie each have their own
adjectives, nouns and syllables, so the same four patterns produce
`Vorthakdur` for metal and `Blueavenue` for jazz.

## Running it

Requires Python 3.10+. The terminal version needs nothing else:

```bash
python band_generator.py
```

The window needs PyQt6:

```bash
pip install -r requirements.txt
python gui.py
```

Both write to the same `favorites.txt`, so a name saved in the window shows up
in the terminal menu and vice versa.

## Project structure

| File | Contains |
|---|---|
| `generator.py` | all the logic — genre data, the four name patterns, favourites file I/O |
| `band_generator.py` | terminal interface: menu, prompts, printing |
| `gui.py` | PyQt6 interface: dropdown, spin box, list, save button |
| `favorites.txt` | saved names, one per line (created on first save, not tracked by git) |

`generator.py` contains no `print` and no `input`. That is the whole design:
the logic reports values, the interface decides how to show them. It is why the
GUI reuses every generation function unchanged, and why the module can be tested
or imported from anywhere:

```python
>>> import generator
>>> generator.generate_many("jazz", 3)
['Mavovo', 'Velvetsession', 'Nesaza']
```

## How it works

`generate_name(genre)` looks the genre's word lists up in `GENRES`, picks one of
four pattern functions at random, and calls it with those words. The pattern
functions are stored in a list — `patterns = [pattern_the_adjective_noun, ...]`
— so adding a fifth naming style means writing one function and adding its name
to that list. Nothing else changes.

`generate_many` collects unique names and gives up after `how_many * 20`
attempts, so asking for more names than a genre can produce returns fewer rather
than looping forever.

## Adding a genre

Pure data — add an entry to `GENRES` in `generator.py`:

```python
"synthwave": {
    "adjectives": ["Neon", "Chrome", "Retro", "Digital", "Endless"],
    "nouns": ["Highway", "Sunset", "Circuit", "Mirage", "Nights"],
    "syllables": ["neo", "vex", "syn", "lux", "dra", "kai", "zen", "ora"],
},
```

The terminal menu and the GUI dropdown both read their options from `GENRES`,
so it appears in each without touching interface code.

## Ideas for later

- Delete favourites (rewriting the file instead of appending to it)
- Store favourites as JSON with genre and date, not just a name
- A favourites tab in the GUI (`QTabWidget`)
- `pytest` tests for `generator.py`

---

Built as a step-by-step Python learning exercise: lists and dicts, functions as
values, exceptions, file I/O, modules, classes, and event-driven GUI code.
