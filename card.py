from treys import Card as TreysCard
class Card:
    treys_sortes = {'pique': 's', 'coeur': 'h', 'carreau': 'd', 'trefle': 'c'}
    face_visible = False

    def __init__(self, figure, sortes, face_visible = False):
        self.figure = figure
        self.types = sortes
        self.face_visible = True

    def __str__(self):
        if self.face_visible:
            return TreysCard.int_to_pretty_str(self.to_treys())
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