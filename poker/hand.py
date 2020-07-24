from poker.validators import (
    RoyalFlushValidator,
    StraightFlushValidator,
    FourOfAKindValidator,
    FullHouseValidator,
    FlushValidator,
    StraightValidator,
    ThreeOfAKindValidator,
    TwoPairValidator,
    PairValidator,
    HighCardValidator,
    NoCardsValidator
)
class Hand():

    VALIDATORS = (
        RoyalFlushValidator,
        StraightFlushValidator,
        FourOfAKindValidator,
        FullHouseValidator,
        FlushValidator,
        StraightValidator,
        ThreeOfAKindValidator,
        TwoPairValidator,
        PairValidator,
        HighCardValidator,
        NoCardsValidator
    )

    def __init__(self):
        self.cards = []

    def __repr__(self):
        cards_as_strings = [str(card) for card in self.cards]
        return ", ".join(cards_as_strings)

    def add_cards(self, cards):
        copy = self.cards[:]
        copy.extend(cards)
        copy.sort()
        self.cards = copy

    def best_rank(self):
        for index, validator_class in enumerate(self.VALIDATORS):
            validator = validator_class(cards = self.cards)
            if validator.is_valid():
                return (index, validator.name, validator.valid_cards())

    # @property
    # def _rank_validations_from_best_to_worst(self):
    #     return (
    #         ("Royal Flush",RoyalFlushValidator(cards = self.cards).is_valid),
    #         ("Straight Flush",StraightFlushValidator(cards = self.cards).is_valid),
    #         ("Four of a Kind",FourOfAKindValidator(cards = self.cards).is_valid),
    #         ("Full House",FullHouseValidator(cards = self.cards).is_valid),
    #         ("Flush",FlushValidator(cards = self.cards).is_valid),
    #         ("Straight",StraightValidator(cards = self.cards).is_valid),
    #         ("Three of a kind", ThreeOfAKindValidator(cards = self.cards).is_valid),
    #         ("Two Pair",TwoPairValidator(cards = self.cards).is_valid),
    #         ("Pair",PairValidator(cards = self.cards).is_valid),
    #         ("High Card",HighCardValidator(cards = self.cards).is_valid),
    #         ("No Cards",NoCardsValidator(cards = self.cards).is_valid)
    #     )
    
    
    
    # def _royal_flush(self):
    #     is_straight_flush = StraightFlushValidator(cards = self.cards).is_valid()
    #     if not is_straight_flush:
    #         return False

    #     is_royal = self.cards[-1].rank == "Ace"
    #     return is_straight_flush and is_royal

    # def _straight_flush(self):
    #     return FlushValidator(cards = self.cards) and StraightValidator(cards = self.cards.is_valid())
    
    # def _four_of_a_kind(self):
    #     ranks_with_four_of_a_kind = self._ranks_with_count(4)
    #     return len(ranks_with_four_of_a_kind) == 1

    # def _full_house(self):
    #     return self._three_of_a_kind() and PairValidator(cards = self.cards).is_valid()
    
    # def _flush(self):
    #     suits_that_occur_5_or_more_times = {
    #         suit: suit_count
    #         for suit,suit_count in self._card_suit_counts.items()
    #         if suit_count >= 5
    #     }
    #     return len(suits_that_occur_5_or_more_times) == 1
    # def _straight(self):

    #     if len(self.cards) < 5:
    #         return False

    #     rank_indexes = [card.rank_index for card in self.cards]
    #     starting_rank_index = rank_indexes[0]
    #     last_rank_index = rank_indexes[-1]
    #     straight_consecutive_indexes = list(
    #         range(starting_rank_index, last_rank_index + 1)
    #     )
    #     return rank_indexes == straight_consecutive_indexes

    # def _three_of_a_kind(self):
    #     ranks_with_three_of_a_kind = self._ranks_with_count(3)
    #     return len(ranks_with_three_of_a_kind) == 1

    # def _two_pair(self):
    #     ranks_with_pairs = self._ranks_with_count(2)
    #     return len(ranks_with_pairs) == 2

    # def _pair(self):
    #     ranks_with_pairs = self._ranks_with_count(2)
    #     return len(ranks_with_pairs) == 1
    
            
    # def _ranks_with_count(self,count):
    #     return {
    #         rank: rank_count
    #         for rank,rank_count in self._card_rank_counts.items()
    #         if rank_count == count
    #     }
    
    # @property
    # def _card_suit_counts(self):
    #     card_suit_counts={}
    #     for card in self.cards:
    #         card_suit_counts.setdefault(card.suit,0)
    #         card_suit_counts[card.suit] +=1
    #     return card_suit_counts
    
    # @property
    # def _card_rank_counts(self):
    #     card_rank_counts={}
    #     for card in self.cards:
    #         card_rank_counts.setdefault(card.rank,0)
    #         card_rank_counts[card.rank] +=1
    #     return card_rank_counts