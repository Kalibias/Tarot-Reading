import random
import json
from word2number import w2n

# Setting up the varibles for future uses.
maj_arcana_id = ['Fool', 'Magician', 'High Priestess', 'Empress', 'Emperor', 'Hierophant', 'Lovers',
                 'Chariot', 'Strength', 'Hermit', 'Wheel of Fortune', 'Justice', 'Hanged Man', 'Death'
                 ]

suit_title = ["Ace", "Two", "Three",
              "Four", "Five", "Six",
              "Seven", "Eight", "Nine", "Ten",
              "Page", "Knight", "Queen", "King"]

min_arcana_id = ["Cups", "Swords", "Pentacles", "Wands"]
card_facing = ["Reversed", "Upright"]

# Assigning Suits to their number to make Iteration easier.
suit_dict = {
    "Ace": 0,
    "Page": 10,
    "Knight": 11,
    "Queen": 12,
    "King": 13
}
maj_dict = {
    "Pentacles": 0,
    "Cups": 1,
    "Swords": 2,
    "Wands": 3
}
maj_dict = {
    "Fool": 0,
    "Magician": 1,
    "High Priestess": 2,
    "Empress": 3,
    "Emperor": 4,
    "Hierophant": 5,
    "Lovers": 6,
    "Chariot": 7,
    "Strength": 8,
    "Hermit": 9,
    "Wheel of Fortune": 10,
    "Justice": 11,
    "Hanged Man": 12,
    "Death": 13

}


def tarot_reading():
    num = random.randint(0, 1)
    if num == 0:
        # Randomize which suit, arcana and layout is selected.
        suit = suit_title[random.randint(0, len(suit_title) - 1)]
        min_arcana = min_arcana_id[random.randint(0, len(min_arcana_id) - 1)]
        facing = card_facing[random.randint(0, len(card_facing) - 1)]

        # Made to specifically pick the JSON file to read and get the Correct reading.
        tarotfile = "Tarot DB/" + min_arcana + ".json"
        f = open(tarotfile, encoding="UTF-8")
        min_data = json.load(f)

        print("Your card is " + suit + " of " + min_arcana + "\nFacing: " + facing)
        if facing == "Upright":
            # Data > Picks the Minor Arcana  > Array placement of suit > Suit itself >
            # placement of meanings > meanings themself
            print(min_data[str(min_arcana)][cover_suit(suit)][suit][0]['key_means'])
            f.close()

        else:
            print(min_data[str(min_arcana)][cover_suit(suit)][suit][0]['rev_means'])
            f.close()

    else:
        # Opening the Major Arcana JSON file for reading
        f = open("Tarot DB/major_arcana.json", encoding="UTF-8")
        maj_data = json.load(f)

        # Randomizing which Major Arcana is picked
        maj_arcana = maj_arcana_id[random.randint(0, len(maj_arcana_id) - 1)]
        facing = card_facing[random.randint(0, len(card_facing) - 1)]

        print("Your card is " + maj_arcana + "\n" + facing)
        if facing == "Upright":
            print(maj_data[int(maj_dict[maj_arcana])][maj_arcana][0]['key_means'])
        else:
            print(maj_data[int(maj_dict[maj_arcana])][maj_arcana][0]['rev_means'])


# Convert words to numbers using the w2n library
def cover_suit(suit):
    if suit == "Ace" or suit == "Page" or suit == "Knight" or suit == "Queen" or suit == "King":
        ans = suit_dict[suit]
        return int(ans)
    else:
        # Subtracting one due to placement of cards.
        ans = w2n.word_to_num(suit) - 1
        return int(ans);


def rerun(int):
    while int != 0:
        tarot_reading()
        int = int - 1


response = input("How many cards would you like to draw? ")
num = w2n.word_to_num(response)
rerun(num)
