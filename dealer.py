class Dealer:
    def __init__(self, deck):
        self.deck = deck

    def distribute_cards(self):
        return [self.deck.draw() for i in range(2)]

    def give_three_cards(self):
        return [self.deck.draw() for i in range(3)]

    def give_card(self):
        return self.deck.draw()