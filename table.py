from dealer import Dealer
from deck import Deck

class Table:
    def __init__(self, name):
        self.name = name
        self.deck = Deck()
        self.dealer = Dealer(self.deck)
        self.players = []

    def add_player(self, player):
        self.players.append(player)
