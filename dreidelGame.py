import Dreidel_Game


def main():
    my_game = Dreidel_Game.DreidelGame()
    my_game.init_game()
    while not my_game.check_for_winner():
        my_game.player_spin()
        print(my_game)
        while my_game.check_for_tie():
            my_game.tie_breaker()
            my_game.player_spin()
            print(my_game)


main()
