import unittest

from poker.card import Card
from poker.validators import StraightFlushValidator

class StraightFlushValidatorTest(unittest.TestCase):
    def test_dtermines_that_there_are_not_five_consecutive_cards_with_same_suit(self):
        cards = [
            Card(rank = "3", suit= "Clubs"),
            Card(rank = "4", suit= "Clubs"),
            Card(rank = "5", suit= "Clubs"),
            Card(rank = "6", suit= "Clubs"),
            Card(rank = "7", suit= "Clubs"),
            Card(rank = "King", suit = "Clubs"),
            Card(rank = "Ace", suit = "Diamonds")
        ]
        
        validator = StraightFlushValidator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

        

    def test_dtermines_that_there_are_not_five_consecutive_cards_with_same_suit(self):
        
        three = Card(rank = "3", suit= "Clubs")
        four = Card(rank = "4", suit= "Clubs")
        five = Card(rank = "5", suit= "Clubs")
        six = Card(rank = "6", suit= "Clubs")
        seven = Card(rank = "7", suit= "Clubs")
        cards = [
            three,
            four,
            five,
            six,
            seven,
            Card(rank = "King", suit = "Clubs"),
            Card(rank = "Ace", suit = "Diamonds")
        ]
        
        validator = StraightFlushValidator(cards = cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                three,
                four,
                five,
                six,
                seven
            ]
        )