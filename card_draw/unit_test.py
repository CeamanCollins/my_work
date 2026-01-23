import unittest
from card_draw import Deck, Hand

class TestCardDraw(unittest.TestCase):

    def setUp(self):
        self.card_deck = Deck()

    def test_deck_initialization(self):
        self.assertIsNotNone(self.card_deck.deck_id)
        self.assertEqual(self.card_deck.cards, 52)

    def test_draw_cards(self):
        drawn_cards = self.card_deck.draw_cards(5)
        self.assertEqual(len(drawn_cards), 5)
        self.assertEqual(self.card_deck.cards, 47)

    def test_pair_detection(self):
        self.hand = Hand(self.card_deck)
        self.hand.cards = [
            {'value': '2', 'suit': 'HEARTS'},
            {'value': '3', 'suit': 'SPADES'},
            {'value': '5', 'suit': 'DIAMONDS'},
            {'value': 'K', 'suit': 'CLUBS'},
            {'value': 'K', 'suit': 'HEARTS'}
        ]
        result = self.hand.check_hand()
        self.assertIn("pair", result)

    def test_three_of_a_kind_detection(self):
        self.hand = Hand(self.card_deck)
        self.hand.cards = [
            {'value': '3', 'suit': 'HEARTS'},
            {'value': '3', 'suit': 'SPADES'},
            {'value': '3', 'suit': 'DIAMONDS'},
            {'value': '8', 'suit': 'CLUBS'},
            {'value': 'J', 'suit': 'HEARTS'}
        ]
        result = self.hand.check_hand()
        self.assertIn("three of a kind", result)

    def test_flush_detection(self):
        self.hand = Hand(self.card_deck)
        self.hand.cards = [
            {'value': '2', 'suit': 'HEARTS'},
            {'value': '5', 'suit': 'HEARTS'},
            {'value': '9', 'suit': 'HEARTS'},
            {'value': 'JACK', 'suit': 'HEARTS'},
            {'value': 'KING', 'suit': 'HEARTS'}
        ]
        result = self.hand.check_hand()
        self.assertIn("flush", result)

    def test_royal_flush_detection(self):
        self.hand = Hand(self.card_deck)
        self.hand.cards = [
            {'value': '10', 'suit': 'SPADES'},
            {'value': 'JACK', 'suit': 'SPADES'},
            {'value': 'QUEEN', 'suit': 'SPADES'},
            {'value': 'KING', 'suit': 'SPADES'},
            {'value': 'ACE', 'suit': 'SPADES'}
        ]
        result = self.hand.check_hand()
        self.assertIn("royal flush", result)

if __name__ == '__main__':
    unittest.main()