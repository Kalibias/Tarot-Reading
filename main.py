import random
import json
import textwrap

# Setting up the variables for future uses.
card_facing = ["Reversed", "Upright"]
tarot_arcana = ["Major", "Minor"]

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


def tarot_draw():
    with open("Tarot DB/Arcana.json", encoding="UTF-8") as tarot:
        tarot = json.load(tarot)
    # Picks the arcana that'll be used to draw the card.
    arcana = random.choice(tarot_arcana)
    facing = random.choice(card_facing)
    meaning = 'key_means' if facing == "Upright" else 'rev_means'
    if arcana == "Major":

        maj_arc = random.choice(list(maj_dict.keys()))
        
        # Renamed variables for better clarity of what they do.
        drawn_card = f"You card is {maj_arc} \n{facing}"

        # Utilizing facing variable to define 'meaning.'

        result = tarot["Major"][int(maj_dict[maj_arc])][maj_arc][0][meaning]

        # Makes the card readable in the console.
        card = "\n".join(textwrap.wrap(result, 90))

    elif arcana == "Minor":

        min_arc = random.choice(list(min_dict.keys()))

        #Added Variable for Minor Arcana.
        suit = random.choice(list(suit_dict.keys()))

        # Adds the Suit variable into the Drawn Card
        drawn_card = f"You card is {suit} of {min_arc} \n{facing}"

        # Suit Dict comes in to easily define which suit was drawn.
        result = tarot["Minor"][min_arc][suit_dict[suit]][suit][0][meaning]
        card = "\n".join(textwrap.wrap(result, 90))

    print(f"{drawn_card}\n{card}")
    return f"{drawn_card}\n {card}"

# For now it'll draw a singular card.
tarot_draw()

