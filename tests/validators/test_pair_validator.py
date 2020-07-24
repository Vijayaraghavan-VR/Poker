import unittest

from poker.card import Card
from poker.validators import PairValidator

class PairValidatorTest(unittest.TestCase):
    def test_figures_out_pair_is_best_rank(self):
        cards = [
            Card(rank = "Ace", suit ="Spades"),
            Card(rank = "Ace", suit = "Clubs")
        ]
        
        validator = PairValidator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_pair_from_card_collection(self):
        ten_of_spades = Card(rank = "10", suit= "Spades")
        ten_of_clubs = Card(rank = "10", suit = "Clubs")

        cards = [
            Card(rank = "3", suit = "Hearts"),
            Card(rank = "5", suit = "Diamonds"),
            ten_of_spades,
            ten_of_clubs,
            Card(rank = "King", suit = "Clubs")
        ]

        validator = PairValidator(cards = cards)

        self.assertEqual(
            validator.valid_cards(),
            [ten_of_spades, ten_of_clubs]
        )