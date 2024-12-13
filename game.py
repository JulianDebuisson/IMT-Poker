class Game:
    def __init__(self, table):
        self.table = table
        self.players = table.players
        self.dealer = table.dealer
        self.cards = []

    def play_game(self):
        for player in self.players:
            player.hand = self.dealer.distribute_cards()

        self.players[0].get_hand()
        print("Vos cartes : ", self.players[0].display_hand())

        for round_nb in range(4):
            self.cards.append([])
            if round_nb == 1:
                self.cards[round_nb] = self.dealer.give_three_cards()
            if round_nb == 2 or round_nb == 3:
                self.cards[round_nb] = self.dealer.give_card()
