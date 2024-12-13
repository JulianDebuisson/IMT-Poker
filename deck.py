import random
from card import Card

class Deck:
    def __init__(self):
        figures = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        sortes = {'pique': '♠', 'coeur': '♥', 'carreau': '♦', 'trefle': '♣'}
        self.cards = []
        for figure in figures:
            for sorte in sortes:
                self.cards.append(Card(figure, sorte))
        random.shuffle(self.cards)

    def draw(self):
        if self.cards:
            return self.cards.pop()
        raise ValueError("La pioche est vide.")