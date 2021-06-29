# Hangman program
# Author: Ernst Fanfan
# date: 06/23/2021
# main
import interface as i

i.start_of_game()
# end of loop
transition_code = 0
while transition_code != 3:
    # no change menu loop
    while transition_code == 0:
        transition_code = i.main_menu()
    # one player game
    while transition_code == 1 or transition_code == 2:
        toggle = 0
        game = object
        if transition_code == 1:
            game = i.setup_single_game()
        if transition_code == 2:
            game = i.setup_two_player_game()
        i.update_ui(game)
        while transition_code == 1 or transition_code == 2:
            i.turn(game.players[toggle], game.mask)
            # switch player
            switcher = {0: 1, 1: 0}
            toggle = switcher.get(toggle)
            transition_code = i.update_ui(game)

        i.ending(game.players)


# ending program
i.end()

