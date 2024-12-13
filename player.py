from treys import Evaluator
class Player:
    def __init__(self, name, jetons = 1000, is_active = True):
        self.name = name
        self.jetons = jetons
        self.is_active = is_active
        self.hand = []
        self.has_bet = 0
        self.has_fold = False

    def set_cards(self, cards):
        self.hand = cards

    def get_has_fold(self):
        return self.has_fold
    
    def set_has_fold(self, has_fold):
        self.has_fold = has_fold

    def get_hand(self):
        for card in self.hand:
            card.turn_card()

    def get_has_bet(self):
        return self.has_bet

    def get_treys_hand(self):
        return [card.to_treys() for card in self.hand]

    def bet(self, amount):
        self.jetons -= amount
        self.has_bet += amount
        return amount

    def get_bet(self):
        return self.has_bet
    
    def add_jetons(self, amount):
        self.jetons += amount
    
    def get_rank(self, board):
        cards = self.get_treys_hand()
        score = Evaluator().evaluate(board=board, hand=cards)
        return score

    def display_hand(self):
        return [str(card) for card in self.hand]