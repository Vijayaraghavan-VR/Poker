from poker.validators import FiveCardRanksInARowValidator

class StraightFlushValidator(FiveCardRanksInARowValidator):
    def __init__(self,cards):
        self.cards = cards 
        self.name = "Straight Flush"

    def is_valid(self):
        for five_cards in self._collections_of_five_straight_cards_in_a_row:
            unique_suits_in_next_five_cards = { card.suit for card in five_cards}
            if len(unique_suits_in_next_five_cards) == 1:
                return True

        return False

    def valid_cards(self):
        return self._straight_flush_card_batches[-1]

    @property
    def _straight_flush_card_batches(self):
        return [
            five_cards
            for five_cards in self._collections_of_five_straight_cards_in_a_row
            if len({ card.suit for card in five_cards }) == 1
        ]

    # @property
    # def _collections_of_five_straight_cards_in_a_row(self):
    #     index = 0
    #     final_index = len(self.cards) - 1
    #     collections_of_five_straight_cards_in_a_row = []

    #     while index + 4 <= final_index:
    #         next_five_cards = self.cards[index: index + 5]
    #         next_five_rank_indices = [card.rank_index for card in next_five_cards]

    #         if self._every_element_increasing_by_1(next_five_rank_indices):
    #             collections_of_five_straight_cards_in_a_row.append(next_five_cards)

    #         index += 1

    #     return collections_of_five_straight_cards_in_a_row

        
     
    # def _every_element_increasing_by_1(self, rank_indexes):
    #     starting_rank_index = rank_indexes[0]
    #     last_rank_index = rank_indexes[-1]
    #     straight_consecutive_indexes = list(
    #         range(starting_rank_index, last_rank_index + 1)
    #     )
    #     return rank_indexes == straight_consecutive_indexes

