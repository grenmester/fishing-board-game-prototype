import random

cards = [
    {
        "name": "Rainbow Trout",
        "requirement": "roll a 2",
        "money": "3",
        "reputation": "4",
        "size": "10",
        "color": "silver",
    },
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
    "habitat": "river"
  },
  {
    "name": "Canary Rockfish",
    "requirement": "roll an even number",
    "money": "5",
    "rarity": "uncommon",
    "size": "50",
    "color": "orange",
    "habitat": "reef"
  },
  {
    "name": "Salmon",
    "requirement": "roll a 3 or 4",
    "money": "6",
    "rarity": "common",
    "size": "70",
    "color": "silver",
    "habitat": "river"
  },
  {
    "name": "Pufferfish",
    "requirement": "roll a 2 and a 5",
    "money": "3",
    "rarity": "uncommon",
    "size": "30",
    "color": "yellow",
    "habitat": "reef"
  },
  {
    "name": "Bluefin Tuna",
    "requirement": "roll a 6",
    "money": "15",
    "rarity": "rare",
    "size": "200",
    "color": "blue",
    "habitat": "ocean"
  },
  {
    "name": "Anglerfish",
    "requirement": "roll doubles",
    "money": "12",
    "rarity": "rare",
    "size": "60",
    "color": "brown",
    "habitat": "deep sea"
  },
  {
    "name": "Clownfish",
    "requirement": "roll a 1 or 6",
    "money": "4",
    "rarity": "common",
    "size": "15",
    "color": "orange",
    "habitat": "reef"
  },
  {
    "name": "Swordfish",
    "requirement": "roll two odd numbers",
    "money": "14",
    "rarity": "rare",
    "size": "150",
    "color": "silver",
    "habitat": "ocean"
  },
  {
    "name": "Goldfish",
    "requirement": "roll a 1",
    "money": "2",
    "rarity": "common",
    "size": "10",
    "color": "gold",
    "habitat": "lake"
  },
  {
    "name": "Catfish",
    "requirement": "roll a 3",
    "money": "5",
    "rarity": "common",
    "size": "60",
    "color": "gray",
    "habitat": "river"
  },
  {
    "name": "Stingray",
    "requirement": "roll two even numbers",
    "money": "8",
    "rarity": "uncommon",
    "size": "120",
    "color": "brown",
    "habitat": "ocean"
  },
  {
    "name": "Mahi Mahi",
    "requirement": "roll a 5 or 6",
    "money": "10",
    "rarity": "uncommon",
    "size": "100",
    "color": "green",
    "habitat": "ocean"
  },
  {
    "name": "Barracuda",
    "requirement": "roll a 4 and a 5",
    "money": "9",
    "rarity": "uncommon",
    "size": "90",
    "color": "silver",
    "habitat": "reef"
  },
  {
    "name": "Perch",
    "requirement": "roll a 2 or 3",
    "money": "3",
    "rarity": "common",
    "size": "25",
    "color": "green",
    "habitat": "lake"
  },
  {
    "name": "Grouper",
    "requirement": "roll a total of 8",
    "money": "11",
    "rarity": "rare",
    "size": "130",
    "color": "brown",
    "habitat": "reef"
  },
  {
    "name": "Tilapia",
    "requirement": "roll any even number",
    "money": "4",
    "rarity": "common",
    "size": "40",
    "color": "silver",
    "habitat": "lake"
  },
  {
    "name": "Snapper",
    "requirement": "roll a 1 and a 4",
    "money": "6",
    "rarity": "uncommon",
    "size": "50",
    "color": "red",
    "habitat": "reef"
  },
  {
    "name": "Halibut",
    "requirement": "roll a 2 or 6",
    "money": "12",
    "rarity": "rare",
    "size": "180",
    "color": "brown",
    "habitat": "ocean"
  },
  {
    "name": "Eel",
    "requirement": "roll a 5",
    "money": "5",
    "rarity": "uncommon",
    "size": "70",
    "color": "black",
    "habitat": "river"
  },
  {
    "name": "Minnow",
    "requirement": "roll a total of 3",
    "money": "1",
    "rarity": "common",
    "size": "5",
    "color": "silver",
    "habitat": "lake"
  },
  {
    "name": "Carp",
    "requirement": "roll a total of 4",
    "money": "3",
    "rarity": "common",
    "size": "60",
    "color": "gold",
    "habitat": "lake"
  },
  {
    "name": "Herring",
    "requirement": "roll two numbers that add to 7",
    "money": "4",
    "rarity": "common",
    "size": "30",
    "color": "silver",
    "habitat": "ocean"
  },
  {
    "name": "Flounder",
    "requirement": "roll two 2s",
    "money": "7",
    "rarity": "uncommon",
    "size": "50",
    "color": "brown",
    "habitat": "ocean"
  },
  {
    "name": "Sardine",
    "requirement": "roll a total of 6",
    "money": "2",
    "rarity": "common",
    "size": "15",
    "color": "silver",
    "habitat": "ocean"
  },
  {
    "name": "Mackerel",
    "requirement": "roll two 3s",
    "money": "5",
    "rarity": "common",
    "size": "35",
    "color": "blue",
    "habitat": "ocean"
  },
  {
    "name": "Sea Bass",
    "requirement": "roll a total of 9",
    "money": "6",
    "rarity": "uncommon",
    "size": "60",
    "color": "black",
    "habitat": "ocean"
  },
  {
    "name": "Cod",
    "requirement": "roll a total of 5",
    "money": "5",
    "rarity": "common",
    "size": "70",
    "color": "brown",
    "habitat": "ocean"
  },
  {
    "name": "Marlin",
    "requirement": "roll a total of 10",
    "money": "16",
    "rarity": "rare",
    "size": "200",
    "color": "blue",
    "habitat": "ocean"
  },
  {
    "name": "King Salmon",
    "requirement": "roll a 6 and a 6",
    "money": "14",
    "rarity": "rare",
    "size": "100",
    "color": "silver",
    "habitat": "river"
  },
  {
    "name": "Whitefish",
    "requirement": "roll a total of 7",
    "money": "4",
    "rarity": "common",
    "size": "45",
    "color": "white",
    "habitat": "lake"
  },
  {
    "name": "Crappie",
    "requirement": "roll a 1 and a 2",
    "money": "3",
    "rarity": "common",
    "size": "25",
    "color": "silver",
    "habitat": "lake"
  },
  {
    "name": "Bluegill",
    "requirement": "roll a total of 11",
    "money": "2",
    "rarity": "common",
    "size": "20",
    "color": "blue",
    "habitat": "lake"
  },
  {
    "name": "Zander",
    "requirement": "roll two odd numbers",
    "money": "7",
    "rarity": "uncommon",
    "size": "60",
    "color": "green",
    "habitat": "river"
  },
  {
    "name": "Pike",
    "requirement": "roll a 4",
    "money": "9",
    "rarity": "uncommon",
    "size": "90",
    "color": "green",
    "habitat": "lake"
  },
  {
    "name": "Bream",
    "requirement": "roll a 1 or 3",
    "money": "3",
    "rarity": "common",
    "size": "30",
    "color": "silver",
    "habitat": "lake"
  },
]

drawn_cards = []


def draw(num):
    if len(cards) < num:
        print("Not enough cards to draw two.")
        return
    drawn = random.sample(cards, num)
    print("You drew:")
    for card in drawn:
        print(f"- {toString(card)}")
    drawn_cards.extend(drawn)


def remove(num):
    if len(drawn_cards) < num:
        print(f"There is no {num}th card to remove.")
        return
    removed = drawn_cards.pop(num - 1)
    print(f"Removed the {num}th card: {removed['name']}")


def roll(num):
    rolls = [str(random.randint(1, 6)) for _ in range(num)]
    print(f"Rolled {', '.join(rolls)}")


def list_cards():
    print("\nCurrent cards:")
    for idx, card in enumerate(drawn_cards, 1):
        print(f"{idx}: {toString(card)}")
    print()

def toString(card):
    return f"{card['name']} ({card['requirement']}) Money: {card['money']}\n    [{card['habitat']}] - {card['size']}cm\n    [{card['rarity'].upper()}] - {card['color']}"

def main():
    print(f"Game Start ({len(cards)} fish)")
    while True:
        command = input(">> ").strip().lower()
        if command.startswith("draw"):
            draw(int(command.split()[-1]))
        elif command.startswith("remove"):
            remove(int(command.split()[-1]))
        elif command.startswith("roll"):
            roll(int(command.split()[-1]))
        elif command == "list":
            list_cards()
        elif command == "quit":
            print("Exiting.")
            break
        else:
            print("Unknown command. Try 'draw 2', 'remove 4', 'list', or 'quit'.")


if __name__ == "__main__":
    main()
