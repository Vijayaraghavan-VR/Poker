class GameRound():
    def __init__(self, deck, players):
        self.deck = deck
        self.players = players
    
    def play(self):
        self.deck.shuffle()
        self._deal_initial_two_cards_to_each_player()
        self._make_bets()

        self._deal_flop_cards()
        self._make_bets() # because, after each and every fold some may will to make bet !

        self._deal_turn_card()
        self._make_bets()

        self._deal_river_card()
        self._make_bets()

    def _shuffle_deck(self):
        self.deck.shuffle()

    # Here we are giving two different cards to each player.

    def _deal_initial_two_cards_to_each_player(self):
        for player in self.players:
            two_cards = self.deck.remove_cards(2)
            player.add_cards(two_cards)

    def _make_bets(self):
        for player in self.players:
            if player.wants_to_fold():
                self.players.remove(player)

    def _deal_community_cards(self, number):
        community_cards = self.deck.remove_cards(number)
        for player in self.players:
            player.add_cards(community_cards)

    # def _deal_flop_cards(self):
    #     community_cards = self.deck.remove_cards(3)
    #     for player in self.players:
    #         player.add_cards(community_cards)
    # I refactor it

    # Here the community card is same for all the players
    def _deal_flop_cards(self):
        self._deal_community_cards(3)

    def _deal_turn_card(self):
        self._deal_community_cards(1)

    def _deal_river_card(self):
        self._deal_community_cards(1)        