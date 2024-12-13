from game import Game
from player import Player
from table import Table

if __name__ == '__main__':
    print("Julian Debuisson - Salsabil Amri")
    player_1 = Player("Joueur 1")
    player_2 = Player("Joueur 2")

    table = Table("Table 1")
    table.add_player(player_1)
    table.add_player(player_2)
    game = Game(table)
    game.play_game()