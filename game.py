from treys import Card

class Game:
    def __init__(self, table):
        self.table = table
        self.players = table.players
        self.dealer = table.dealer
        self.cards = []

    def play_game(self):
        for player in self.players:
            player.hand = self.dealer.distribute_cards()

        for player in self.players:
            print(player.name, " : ", player.display_hand())

        for round_nb in range(3):

            if round_nb == 0:
                self.cards += self.dealer.give_three_cards()
            if round_nb == 1 or round_nb == 2:
                self.cards.append(self.dealer.give_card())
            for player in self.table.players:
                if player.has_fold:
                    continue

                self.play_round(player)

            while not self.table.same_bet():
                for player in self.players:
                    if player.has_fold:
                        continue
                    self.play_round(player)
                    if self.table.same_bet():
                        break

        print("\n---------------------------\n")
        print("Board : ", self.cards_to_str())
        print("Pot : ", self.table.pot)
        scores = self.table.get_all_ranks(self.get_trey_hand())
        print("scores : ",scores)
        winners = self.table.get_winner(scores)
        print( winners, " gagne le pot de ", self.table.pot)
        for player in self.table.players:
            if player.name in winners:
                player.add_jetons(self.table.pot/len(winners))

        self.table.verify_elimination()

        if len(self.table.players) == 1:
            print("Le joueur ", self.table.players[0].name, " a gagné la partie")
            exit()
        else:
            self.table.reset()
            self.players = self.table.players
            self.dealer = self.table.dealer
            self.cards = []
            self.play_game()


    def play_round(self, player):
        self.display_info(player)
        if player.has_bet < self.table.max_bet:
            self.handle_bet(player)
        else:
            self.handle_check_or_fold(player)

    def handle_bet(self, player):
        min_bet = self.table.max_bet - player.has_bet
        if player.jetons <= min_bet and player.jetons > 0:
            print("Voulez-vous faire tapie ? (si non, vous vous couchez)")
            prompt = input()
            while prompt != 't' and prompt != 'c':
                print("Entrez un valeur correcte : t ou c")
                prompt = input()
            self.play_bet(player, player.jetons)
            return
            
        print("Combien voulez-vous miser ou vous coucher ? (min : ", min_bet, ")")
        amount = input()
        while (amount != 'c') and (amount != 'ch') and (amount.isdigit() and int(amount) < min_bet):
            print("Entrez un valeur correcte : c ; ch ; ou montant")
            amount = input()
        if amount == 'c':
            player.has_fold = True
            return
        else:
            amount = int(amount)
            while amount > player.jetons or amount < min_bet:
                print("Vous n'avez pas assez de jetons ou vous n'avez pas misé assez")
                prompt = input()
                if prompt.isdigit():
                    amount = int(prompt)
            self.play_bet(player, amount)

    def handle_check_or_fold(self, player):
        print("Combien voulez-vous miser, checker ou vous coucher ?")
        amount = input()
        while (amount != 'c') and (not amount.isdigit()) and (amount != 'ch'):
            print("Entrez un valeur correcte : c ; ch ; ou montant")
            amount = input()
        if amount == 'c':
            player.has_fold = True
            return
        elif amount == 'ch':
            return
        else:
            amount = int(amount)
            while amount > player.jetons:
                print("Vous n'avez pas assez de jetons")
                prompt = input()
                if prompt.isdigit():
                    amount = int(prompt)
            self.play_bet(player, amount)

    def play_bet(self, player, amount):
        player.bet(amount)
        self.table.pot += amount
        self.table.max_bet = player.get_bet()

    def display_info(self, player):
        print("\n---------------------------\n")
        print(player.name, " : ", player.display_hand())
        print("Board : ", self.cards_to_str())
        print("Pot : ", self.table.pot)
        print("Jetons : ", player.jetons)

    def get_trey_hand(self):
        return [card.to_treys() for card in self.cards]
    

    def cards_to_str(self):
        return Card.ints_to_pretty_str([card.to_treys() for card in self.cards])


