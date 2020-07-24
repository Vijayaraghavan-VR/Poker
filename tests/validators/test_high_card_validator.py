import unittest

from poker.card import Card
from poker.validators import HighCardValidator

class HighCardValidatorTest(unittest.TestCase):
    def test_figures_out_high_card_is_best_rank(self):
        cards = [
            Card(rank = "Ace", suit = "Diamonds"),
            Card(rank = "7",suit = "Clubs")
        ]

        validator = HighCardValidator(cards = cards)
    
        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_high_card_from_card_collection(self):
        ace_of_diamonds = Card(rank = "5", suit = "Diamonds")

        cards = [
            Card(rank = "5", suit = "Spades"),
            Card(rank = "8", suit = "Spades"),
            Card(rank = "10", suit = "Spades"),
            Card(rank = "Queen", suit = "Spades"),
            ace_of_diamonds
        ]

        validator = HighCardValidator(cards = cards)

        self.assertEqual(
            validator.valid_cards(),
            [ace_of_diamonds]
        )