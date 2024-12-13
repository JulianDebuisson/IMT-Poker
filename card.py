from treys import Card as TreysCard
class Card:
    figures = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    sortes = {'pique': '♠', 'coeur': '♥', 'carreau': '♦', 'trefle': '♣'}
    treys_sortes = {'pique': 's', 'coeur': 'h', 'carreau': 'd', 'trefle': 'c'}
    face_visible = False

    def __init__(self, figure, sortes, face_visible = False):
        self.figure = figure
        self.types = sortes
        self.face_visible = face_visible

    def __str__(self):
        if self.face_visible:
            return self.figure + self.sortes[self.types]
        else:
            return '??'

    def turn_card(self):
        self.face_visible = not self.face_visible
        return self

    def to_treys(self):
        rank_map = {'10': 'T', 'J': 'J', 'Q': 'Q', 'K': 'K', 'A': 'A'}
        rank = rank_map.get(self.figure, self.figure)
        suit = self.treys_sortes[self.types]

        return TreysCard.new(f"{rank}{suit}")