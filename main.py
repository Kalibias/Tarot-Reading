import random
import json
from word2number import w2n
import textwrap

# Setting up the variables for future uses.
card_facing = ["Reversed", "Upright"]

# Assigning Suits to their number to make Iteration easier.
suit_dict = {
    "Ace": 0,
    "Two": 1,
    "Three": 2,
    "Four": 3,
    "Five": 4,
    "Six": 5,
    "Seven": 6,
    "Eight": 7,
    "Nine": 8,
    "Ten": 9,
    "Page": 10,
    "Knight": 11,
    "Queen": 12,
    "King": 13
}
min_dict = {
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


def min_reading():
    # Randomize which suit, arcana and layout is selected.
    suit = random.choice(list(suit_dict.keys()))
    min_arcana = random.choice(list(min_dict.keys()))
    facing = random.choice(card_facing)

    # Made to specifically pick the JSON file to read and get the Correct reading.

    with open("Tarot DB/minor_arcana.json", encoding="UTF-8") as min_tarot:
        min_data = json.load(min_tarot)

    first = "Your card is " + suit + " of " + min_arcana + "\nFacing: " + facing
    s_key = 'key_means' if facing == "Upright" else 'rev_means'
    result = min_data[min_arcana][suit_dict[suit]][suit][0][s_key]
    second = "\n".join(textwrap.wrap(result, 35))
    return first + "\n" + second


def maj_reading():
    # Opening the Major Arcana JSON file for reading
    with open("Tarot DB/major_arcana.json", encoding="UTF-8") as maj_tarot:
        maj_data = json.load(maj_tarot)

    # Randomizing which Major Arcana is picked
    maj_arcana = random.choice(list(maj_dict.keys()))
    facing = random.choice(card_facing)
    # Printing the
    first = "Your card is " + maj_arcana + "\n" + facing

    #
    s_key = 'key_means' if facing == "Upright" else 'rev_means'
    result = maj_data[int(maj_dict[maj_arcana])][maj_arcana][0][s_key]
    second = "\n".join(textwrap.wrap(result, 35))
    return first + "\n" + second


def tarot_reading(i_int):
    while i_int != 0:
        tarot = [min_reading, maj_reading]
        print(random.choice(tarot)())
        i_int -= 1


response = input("How many cards would you like to draw? ")
amount = w2n.word_to_num(response)
tarot_reading(amount)
