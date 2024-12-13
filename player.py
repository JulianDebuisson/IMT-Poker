class Player:
    def __init__(self, name, jetons = 1000, is_active = True):
        self.name = name
        self.jetons = jetons
        self.is_active = is_active
        self.hand = []

    def set_cards(self, cards):
        self.hand = cards

    def get_hand(self):
        for card in self.hand:
            card.turn_card()

    def display_hand(self):
        return ', '.join(str(card) for card in self.hand)