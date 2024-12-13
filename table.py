from dealer import Dealer
from deck import Deck
from player import Player

class Table:
    def __init__(self, name):
        self.name = name
        self.deck = Deck()
        self.dealer = Dealer(self.deck)
        self.players = []
        self.pot = 0
        self.max_bet = 0

    def add_player(self, player : Player):
        self.players.append(player)

    def bet_players(self, player : Player, amout):
        player.bet(amout)

    def get_all_ranks(self, board):
        return {player.name: player.get_rank(board) for player in self.players}

    def get_winner(self, scores):
        best_rank = min(scores.values())
        return [name for name, rank in scores.items() if rank == best_rank]
    
    def fold(self, player : Player):
        self.players.remove(player)

    def reset(self):
        self.pot = 0
        self.max_bet = 0
        for player in self.players:
            player.has_bet = 0
            player.has_fold = False
            player.hand = []
        self.deck = Deck()
        self.dealer = Dealer(self.deck)
        self.cards = []

    def get_trey_hand(self):
        return [card.to_treys() for card in self.hand]
    
    def verify_elimination(self):
        for player in self.players:
            if player.jetons == 0:
                self.players.remove(player)
                print("Le joueur ", player.name, " a été éliminé")

    def same_bet(self):
        print(len(set([player.get_bet() for player in self.players])) == 1)
        return len(set([player.get_bet() for player in self.players])) == 1
