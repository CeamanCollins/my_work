import requests

class Menu:
    def display(self):
        print("Welcome to the Card Draw Simulator!")
        while True:
            print("\n1. Draw a hand of 5 cards")
            print("2. Check hand for combinations")
            print("3. Exit")
            menu_input = input("Please select an option: ")
            print()
            if menu_input == "1":
                deck = Deck()
                hand = Hand(deck)
                hand.print_hand()
                hand.print_feedback()
            elif menu_input == "2":
                try:
                    card_list = self.split_card_input()
                    if len(card_list) != 5:
                        print("Please enter exactly 5 cards.")
                        continue
                except ValueError:
                    print(f"Invalid input format. Please enter cards in the correct format.")
                    continue
                hand = Hand.__new__(Hand)
                hand.cards = card_list
                try:
                    hand.print_hand()
                    hand.print_feedback()
                except KeyError:
                    print(f"Invalid card value or suit in the input. Please check your entries.")
            elif menu_input == "3":
                print("Exiting the program. Goodbye!")
                exit()

    def split_card_input(self):
        input_cards = input("Enter 5 cards in the format 'value:suit' separated by commas (e.g. '2:H,3:S,5:D,K:C,K:H'): ")
        card_list = []
        for card in input_cards.split(","):
            value, suit = card.split(":")
            letter_to_value = {"J":"JACK","Q":"QUEEN","K":"KING","A":"ACE","1":"ACE"}
            letter_to_suit = {"H":"HEARTS","D":"DIAMONDS","S":"SPADES","C":"CLUBS"}
            card_list.append({'value': letter_to_value.get(value.upper(), value.upper()), 'suit': letter_to_suit.get(suit.upper(), suit.upper())})
        return card_list


class Deck:
    def __init__(self):
        self.deck_id = None
        self.cards = []
        self.initialize_deck()

    def initialize_deck(self):
        url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
        response = requests.get(url)
        data = response.json()
        self.deck_id = data["deck_id"]
        self.cards = data["remaining"]

    def draw_cards(self, count):
        url = f"https://deckofcardsapi.com/api/deck/{self.deck_id}/draw/?count={count}"
        response = requests.get(url)
        data = response.json()
        drawn_cards = data['cards']
        self.cards -= count
        return drawn_cards

class Hand:
    def __init__(self, deck: Deck):
        self.cards = deck.draw_cards(5)

    def print_hand(self):
        print(self)

    def print_feedback(self):
        result = self.check_hand()
        self.feedback(result)

    def check_hand(self):
        values = set()
        suits = set()
        self.repeated_values = []

        for card in self.cards:
            if card['value'] in values:
                self.repeated_values.append(card['value'])
            else:
                values.add(f"{card['value']}")
            suits.add(f"{card['suit']}")

        values_to_number = {"JACK":"11","QUEEN":"12","KING":"13","ACE":"14", "J":"11", "Q":"12", "K":"13", "A":"14"}
        for value in values:
            if value in values_to_number.keys():
                values.remove(value)
                values.add(values_to_number[value])
        result = []

        if len(values) == 4:
            result.append("pair")

        if len(values) == 3:
            if self.repeated_values[0] == self.repeated_values[1]:
                result.append("three of a kind")
            else:
                result.append("two pairs")

        if len(values) == 2:
            if self.repeated_values[0] == self.repeated_values[1] == self.repeated_values[2]:
                result.append("four of a kind")
            else:
                result.append("full house")

        if len(suits) == 1:
            sorted_integers = sorted([int(x) for x in values])
            if sorted_integers == [10, 11, 12, 13, 14]:
                result.append("royal flush")
            elif "royal flush" not in result:
                result.append("flush")

        if len(values) == 5:
            sorted_integers = sorted([int(x) for x in values])
            if sorted_integers[0] + 4 == sorted_integers[1] + 3 == sorted_integers[2] + 2 == sorted_integers[3] + 1 == sorted_integers[4]:
                result.append("straight")
            elif sorted_integers == [2,3,4,5,14]:
                result.append("straight")

        if len(result) == 0:
            highest_value = max([int(x) for x in values])
            number_to_value = {14:"ACE",13:"KING",12:"QUEEN",11:"JACK"}
            self.high_card = number_to_value.get(highest_value, str(highest_value)).capitalize()
            result.append(f"high card")

        return result
    
    def __str__(self):
        suit_symbols = {"SPADES":"♠", "DIAMONDS":"♦", "HEARTS":"♥", "CLUBS":"♣"}
        card_strings = []
        for card in self.cards:
            card_strings.append(f"{card['value'].capitalize()}\t{suit_symbols[card['suit']]} {card['suit'].capitalize()}")
        return "\n".join(card_strings)
    
    def feedback(self, result):
        if "pair" in result:
            print(f"You have drawn a pair of {self.repeated_values[0].capitalize()}s. Congratulations!")
        
        elif "three of a kind" in result:
            print("You have drawn three of a kind. Congratulations!")

        elif "two pairs" in result:
            print("You have drawn two pairs. Congratulations!")

        elif "four of a kind" in result:
            print("You have drawn four of a kind. Congratulations!")

        elif "full house" in result:
            print("You have drawn a full house. Congratulations!")

        elif "flush" in result and "royal flush" not in result:
            print("You have drawn a flush. Congratulations!")

        elif "royal flush" in result:
            print("You have drawn a royal flush. Congratulations!")

        elif "straight" in result and "royal flush" not in result and "flush" not in result:
            print("You have drawn a straight. Congratulations!")

        elif "straight" in result and "flush" in result:
            print("You have drawn a straight flush. Congratulations!")

        elif "high card" in result:
            print(f"You have drawn a high card: {self.high_card}. Better luck next time!")

if __name__ == "__main__":
    Menu().display()