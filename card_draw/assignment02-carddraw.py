import requests

# Getting a fresh deck
deck_url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
deck_response = requests.get(deck_url)
deck_data = deck_response.json()
deck_id = deck_data["deck_id"]

# Drawing 5 cards
deal_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
deal_response = requests.get(deal_url)
deal_data = deal_response.json()
cards = deal_data['cards']

values = set()
suits = set()
repeated_values = []

suit_symbols = {"SPADES":"♠", "DIAMONDS":"♦", "HEARTS":"♥", "CLUBS":"♣"}

# Printing drawn cards and generate sets and for later use
for card in cards:
    print(f"{card['value'].capitalize()} \t {suit_symbols[card['suit']]} {card['suit'].capitalize()}")
    if card['value'] in values:
        repeated_values.append(card['value'])
    else:
        values.add(f"{card['value']}")
    suits.add(f"{card['suit']}")

# Replace words with numbers in values set
values_to_replace = {"JACK":"11","QUEEN":"12","KING":"13","ACE":"14"}
for value in values:
    if value in values_to_replace.keys():
        values.remove(value)
        values.add(values_to_replace[value])

# Detecting a pair
if len(values) == 4:
    print(f"You have drawn a pair of {repeated_values[0].capitalize()}s. Congratulations!")

# Detecting three of a kind and two pairs
if len(values) == 3:
    if repeated_values[0] == repeated_values[1]:
        print("You have drawn three of a kind. Congratulations!")
    else:
        print("You have drawn two pairs. Congratulations!")

# Detecting four of a kind or a full house
if len(values) == 2:
    if repeated_values[0] == repeated_values[1] == repeated_values[2]:
        print("You have drawn four of a kind. Congratulations!")
    else:
        print("You have drawn a full house. Congratulations!")

# Detecting flush or royal flush
if len(suits) == 1:
    sorted_integers = sorted({int(x) for x in values})
    if sorted_integers == [10, 11, 12, 13, 14]:
        print("You have drawn a royal flush. Congratulations!")
    else:
        print("You have drawn a flush. Congratulations!")

# Detecting straight and ace low straight
if len(values) == 5:
    sorted_integers = sorted({int(x) for x in values})
    if sorted_integers[0] + 4 == sorted_integers[1] + 3 == sorted_integers[2] + 2 == sorted_integers[3] + 1 == sorted_integers[4]:
        print("You have drawn a straight. Congratulations!")
    elif sorted_integers == [2,3,4,5,14]:
        print("You have drawn a straight. Congratulations!")