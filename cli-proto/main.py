import random
import cmd

cards = [
    {"name": "Rainbow Trout", "requirement": "roll a 2"},
    {"name": "Canary Rockfish", "requirement": "roll an even number"},
    {"name": "Salmon", "requirement": "roll a 3 or 4"},
    {"name": "Pufferfish", "requirement": "roll a 2 and a 5"},
    {"name": "Bluefin Tuna", "requirement": "roll a total of 10 or higher"},
    {"name": "Anchovy", "requirement": "roll any single number"},
    {"name": "Halibut", "requirement": "roll two matching numbers"},
    {"name": "Mahi-Mahi", "requirement": "roll a 6 and an even number"},
    {"name": "Barracuda", "requirement": "roll a 1 and a 6"},
    {"name": "Clownfish", "requirement": "roll only odd numbers"},
    {"name": "Giant Squid", "requirement": "roll three dice totaling exactly 15"},
    {"name": "Swordfish", "requirement": "roll two dice that sum to 7"},
    {"name": "Stingray", "requirement": "roll a 4 or 5 on all dice"},
    {
        "name": "Electric Eel",
        "requirement": "roll one die that is a 3, and another that is a multiple of 3",
    },
    {"name": "Sunfish", "requirement": "roll three even numbers"},
    {"name": "Goblin Shark", "requirement": "roll a 1, 3, and 5"},
    {"name": "Flying Fish", "requirement": "roll a 6 on your first die"},
    {"name": "Lionfish", "requirement": "roll a pair and a 1"},
    {"name": "Coelacanth", "requirement": "roll a total of exactly 18 with three dice"},
    {"name": "Herring", "requirement": "roll a 1 or 2"},
    {"name": "Archerfish", "requirement": "roll a 4 and a number less than 4"},
    {"name": "Koi", "requirement": "roll two 3s"},
    {"name": "Tilapia", "requirement": "roll three numbers under 5"},
    {
        "name": "Zebra Turkeyfish",
        "requirement": "roll alternating even and odd numbers",
    },
    {"name": "White Sturgeon", "requirement": "roll a 6 and a 6"},
    {"name": "Yellowfin Tuna", "requirement": "roll a total of exactly 12"},
    {"name": "Eelpout", "requirement": "roll a 2, 2, and 4"},
    {"name": "Blobfish", "requirement": "roll three of the same number"},
    {"name": "Sea Bass", "requirement": "roll a 3 and a 5"},
    {"name": "Mackerel", "requirement": "roll a 2, 4, and 6"},
    {"name": "Lanternfish", "requirement": "roll at least one 1"},
    {"name": "Flounder", "requirement": "roll a total of 8"},
    {"name": "Marlin", "requirement": "roll a 6 followed by a 1"},
    {"name": "Bonito", "requirement": "roll two numbers that differ by 1"},
    {"name": "Drum", "requirement": "roll two 4s"},
    {"name": "Cuttlefish", "requirement": "roll three odd numbers"},
    {"name": "Needlefish", "requirement": "roll two dice that add up to 11"},
    {"name": "Tetra", "requirement": "roll a 1, 2, 3"},
    {"name": "Triggerfish", "requirement": "roll a 5 and an odd number"},
    {"name": "Rock Greenling", "requirement": "roll two 2s"},
    {"name": "Spiny Dogfish", "requirement": "roll two dice that sum to 9"},
    {"name": "Wahoo", "requirement": "roll a 3 and a number that’s double it"},
    {"name": "Lungfish", "requirement": "roll three numbers that sum to 9"},
    {"name": "Sardine", "requirement": "roll a total of 6"},
    {"name": "Snapper", "requirement": "roll a 5 or a 6"},
    {"name": "Tilefish", "requirement": "roll three dice, all different"},
    {"name": "Pollock", "requirement": "roll two even numbers"},
    {"name": "Catfish", "requirement": "roll a 2 and a 6"},
    {"name": "Pike", "requirement": "roll any pair"},
    {"name": "Perch", "requirement": "roll a 3 and any even number"},
    {"name": "Bass", "requirement": "roll a 5 and any number lower than 3"},
    {"name": "Smelt", "requirement": "roll a 1 and a 2"},
    {"name": "Red Drum", "requirement": "roll a 4, 4, and 2"},
    {"name": "Gar", "requirement": "roll a 6 and any other 6"},
    {
        "name": "Bream",
        "requirement": "roll two dice with the same parity (both odd or both even)",
    },
    {"name": "Scorpionfish", "requirement": "roll a 1, 2, 4"},
    {"name": "Croaker", "requirement": "roll a 5 and a number not equal to 5"},
    {"name": "Ghost Fish", "requirement": "roll a total divisible by 6"},
    {"name": "Icefish", "requirement": "roll all 1s or all 6s"},
    {"name": "Black Cod", "requirement": "roll three consecutive numbers"},
    {"name": "Ocean Sunfish", "requirement": "roll three 5s"},
]

cards = [
    {
        "name": "Rainbow Trout",
        "requirement": "roll a 2",
        "money": "4",
        "rarity": "common",
        "size": "40",
        "color": "silver",
        "habitat": "river",
    },
    {
        "name": "Canary Rockfish",
        "requirement": "roll an even number",
        "money": "5",
        "rarity": "uncommon",
        "size": "50",
        "color": "orange",
        "habitat": "reef",
    },
    {
        "name": "Salmon",
        "requirement": "roll a 3 or 4",
        "money": "6",
        "rarity": "common",
        "size": "70",
        "color": "silver",
        "habitat": "river",
    },
    {
        "name": "Pufferfish",
        "requirement": "roll a 2 and a 5",
        "money": "3",
        "rarity": "uncommon",
        "size": "30",
        "color": "yellow",
        "habitat": "reef",
    },
    {
        "name": "Bluefin Tuna",
        "requirement": "roll a 6",
        "money": "15",
        "rarity": "rare",
        "size": "200",
        "color": "blue",
        "habitat": "ocean",
    },
    {
        "name": "Anglerfish",
        "requirement": "roll doubles",
        "money": "12",
        "rarity": "rare",
        "size": "60",
        "color": "brown",
        "habitat": "deep sea",
    },
    {
        "name": "Clownfish",
        "requirement": "roll a 1 or 6",
        "money": "4",
        "rarity": "common",
        "size": "15",
        "color": "orange",
        "habitat": "reef",
    },
    {
        "name": "Swordfish",
        "requirement": "roll two odd numbers",
        "money": "14",
        "rarity": "rare",
        "size": "150",
        "color": "silver",
        "habitat": "ocean",
    },
    {
        "name": "Goldfish",
        "requirement": "roll a 1",
        "money": "2",
        "rarity": "common",
        "size": "10",
        "color": "gold",
        "habitat": "lake",
    },
    {
        "name": "Catfish",
        "requirement": "roll a 3",
        "money": "5",
        "rarity": "common",
        "size": "60",
        "color": "gray",
        "habitat": "river",
    },
    {
        "name": "Stingray",
        "requirement": "roll two even numbers",
        "money": "8",
        "rarity": "uncommon",
        "size": "120",
        "color": "brown",
        "habitat": "ocean",
    },
    {
        "name": "Mahi Mahi",
        "requirement": "roll a 5 or 6",
        "money": "10",
        "rarity": "uncommon",
        "size": "100",
        "color": "green",
        "habitat": "ocean",
    },
    {
        "name": "Barracuda",
        "requirement": "roll a 4 and a 5",
        "money": "9",
        "rarity": "uncommon",
        "size": "90",
        "color": "silver",
        "habitat": "reef",
    },
    {
        "name": "Perch",
        "requirement": "roll a 2 or 3",
        "money": "3",
        "rarity": "common",
        "size": "25",
        "color": "green",
        "habitat": "lake",
    },
    {
        "name": "Grouper",
        "requirement": "roll a total of 8",
        "money": "11",
        "rarity": "rare",
        "size": "130",
        "color": "brown",
        "habitat": "reef",
    },
    {
        "name": "Tilapia",
        "requirement": "roll any even number",
        "money": "4",
        "rarity": "common",
        "size": "40",
        "color": "silver",
        "habitat": "lake",
    },
    {
        "name": "Snapper",
        "requirement": "roll a 1 and a 4",
        "money": "6",
        "rarity": "uncommon",
        "size": "50",
        "color": "red",
        "habitat": "reef",
    },
    {
        "name": "Halibut",
        "requirement": "roll a 2 or 6",
        "money": "12",
        "rarity": "rare",
        "size": "180",
        "color": "brown",
        "habitat": "ocean",
    },
    {
        "name": "Eel",
        "requirement": "roll a 5",
        "money": "5",
        "rarity": "uncommon",
        "size": "70",
        "color": "black",
        "habitat": "river",
    },
    {
        "name": "Minnow",
        "requirement": "roll a total of 3",
        "money": "1",
        "rarity": "common",
        "size": "5",
        "color": "silver",
        "habitat": "lake",
    },
    {
        "name": "Carp",
        "requirement": "roll a total of 4",
        "money": "3",
        "rarity": "common",
        "size": "60",
        "color": "gold",
        "habitat": "lake",
    },
    {
        "name": "Herring",
        "requirement": "roll two numbers that add to 7",
        "money": "4",
        "rarity": "common",
        "size": "30",
        "color": "silver",
        "habitat": "ocean",
    },
    {
        "name": "Flounder",
        "requirement": "roll two 2s",
        "money": "7",
        "rarity": "uncommon",
        "size": "50",
        "color": "brown",
        "habitat": "ocean",
    },
    {
        "name": "Sardine",
        "requirement": "roll a total of 6",
        "money": "2",
        "rarity": "common",
        "size": "15",
        "color": "silver",
        "habitat": "ocean",
    },
    {
        "name": "Mackerel",
        "requirement": "roll two 3s",
        "money": "5",
        "rarity": "common",
        "size": "35",
        "color": "blue",
        "habitat": "ocean",
    },
    {
        "name": "Sea Bass",
        "requirement": "roll a total of 9",
        "money": "6",
        "rarity": "uncommon",
        "size": "60",
        "color": "black",
        "habitat": "ocean",
    },
    {
        "name": "Cod",
        "requirement": "roll a total of 5",
        "money": "5",
        "rarity": "common",
        "size": "70",
        "color": "brown",
        "habitat": "ocean",
    },
    {
        "name": "Marlin",
        "requirement": "roll a total of 10",
        "money": "16",
        "rarity": "rare",
        "size": "200",
        "color": "blue",
        "habitat": "ocean",
    },
    {
        "name": "King Salmon",
        "requirement": "roll a 6 and a 6",
        "money": "14",
        "rarity": "rare",
        "size": "100",
        "color": "silver",
        "habitat": "river",
    },
    {
        "name": "Whitefish",
        "requirement": "roll a total of 7",
        "money": "4",
        "rarity": "common",
        "size": "45",
        "color": "white",
        "habitat": "lake",
    },
    {
        "name": "Crappie",
        "requirement": "roll a 1 and a 2",
        "money": "3",
        "rarity": "common",
        "size": "25",
        "color": "silver",
        "habitat": "lake",
    },
    {
        "name": "Bluegill",
        "requirement": "roll a total of 11",
        "money": "2",
        "rarity": "common",
        "size": "20",
        "color": "blue",
        "habitat": "lake",
    },
    {
        "name": "Zander",
        "requirement": "roll two odd numbers",
        "money": "7",
        "rarity": "uncommon",
        "size": "60",
        "color": "green",
        "habitat": "river",
    },
    {
        "name": "Pike",
        "requirement": "roll a 4",
        "money": "9",
        "rarity": "uncommon",
        "size": "90",
        "color": "green",
        "habitat": "lake",
    },
    {
        "name": "Bream",
        "requirement": "roll a 1 or 3",
        "money": "3",
        "rarity": "common",
        "size": "30",
        "color": "silver",
        "habitat": "lake",
    },
]

drawn_cards = []


def to_string(card):
    return f"{card['name']} ({card['requirement']}) Money: {card['money']}\n    [{card['habitat']}] - {card['size']}cm\n    [{card['rarity'].upper()}] - {card['color']}"


class GameShell(cmd.Cmd):
    intro = "Welcome to the fishing board game prototype shell. \nType help or ? to list commands.\n"
    prompt = ">> "

    def do_draw(self, arg):
        "Draw N random cards: draw 3"
        try:
            n = int(arg)
            if n > len(cards):
                print(f"Not enough cards to draw {n}. Only {len(cards)} available.")
                return
            drawn = random.sample(cards, n)
            print("You drew:")
            for card in drawn:
                print(f"- {to_string(card)}")
            drawn_cards.extend(drawn)
        except ValueError:
            print("Usage: draw <number>")

    def do_remove(self, arg):
        "Remove one or more cards by index: remove 2 4 5"
        try:
            indices = sorted(set(int(i) for i in arg.split()), reverse=True)
            if not indices:
                print("Usage: remove <index> [<index> ...]")
                return
            for i in indices:
                if i < 1 or i > len(drawn_cards):
                    print(
                        f"Invalid index {i}. Must be between 1 and {len(drawn_cards)}."
                    )
                    return
            for i in indices:
                removed = drawn_cards.pop(i - 1)
                print(f"Removed card {i}: {removed['name']}")
        except ValueError:
            print("Usage: remove <index> [<index> ...]")

    def do_list(self, _):
        "List all cards"
        for idx, card in enumerate(drawn_cards, 1):
            print(f"{idx}: {to_string(card)}")

    def do_roll(self, arg):
        "Roll N dice: roll 3"
        try:
            n = int(arg)
            if n < 1:
                print("You must roll at least one die.")
                return
            rolls = [str(random.randint(1, 6)) for _ in range(n)]
            print(f"Rolled {', '.join(rolls)}")
        except ValueError:
            print("Usage: roll <number>")

    def do_quit(self, _):
        "Exit the game"
        return True

    def default(self, line):
        print(f"Unknown command: {line}. Type ? to list commands.")


if __name__ == "__main__":
    GameShell().cmdloop()
