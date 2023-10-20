import json, random


def tarot_pull():
    love, career, money = False, False, False
    arcana = random.choice(("Major", "Minor"))
    facing = random.choice(("Upright", "Reversed"))
    side = 'reg' if facing == "Upright" else "rev"
    tarot = json.load(open("DBs/tarot.json"))

    if arcana == "Major":
        arc = random.choice(list(tarot["Major"].keys()))
        card = f"Your card is {facing} {arc} "

        if love == True:
            result = tarot["Major"][arc]["love"]
        if career == True:
            result = tarot["Major"][arc]["career"]
        if money == True:
            result = tarot["Major"][arc]["money"]


        result = tarot["Major"][arc][side]

    if arcana == "Minor":
        arc = random.choice(list(tarot["Minor"].keys()))
        suit = random.choice(list(tarot["Minor"][arc].keys()))
        card = f"Your card is {facing} {suit} of {arc}"
        result = tarot["Minor"][arc][suit][side]

    print(f"{card} \n{result}")
    return f'{card}\n{result}'


def prompt():
    number = int(input("how many times do you want to roll? 0 - 10: "))
    while number > 0:
        tarot_pull()
        number -= 1

prompt()