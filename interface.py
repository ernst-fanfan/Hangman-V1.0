import Game
import TopLevelStates as Tl
import time as t
from Game import Player
from Images import Img


def start_of_game():
    Tl.clear()
    print("""
Welcome to Hangman V1.0!
by: Just Ernst""")
    t.sleep(2)


def main_menu():
    Tl.clear()
    print("""
How many Player?
    1 One Player
    2 Two Player
    3 Exit
    """)
    answer = input("\tEnter 1,2 or 3: ")
    t.sleep(1)
    return Tl.menu_answer_checker(answer)


def setup_two_player_game():
    Tl.clear()
    game = Tl.two_players()
    # collect player one name
    name0 = input("Player one Name: ")
    player_one = Player(1, name0)
    # collect player two name
    name1 = input("Player two Name: ")
    player_two = Player(1, name1)
    # assign players to game
    players = [player_one, player_two]
    game.players = players
    t.sleep(1)
    return game


def setup_single_game():
    Tl.clear()
    game = Tl.one_player()
    # collect player name
    name = input("Name: ")
    player_one = Player(1, name)
    # setup ai
    computer = Player(0, "AI")
    computer.brain.isolate(game.mask)
    # assign players to game
    players = [player_one, computer]
    game.players = players
    t.sleep(1)
    return game


def update_ui(game):
    Tl.clear()
    transition_code = game.update()
    p1 = game.players[0]
    p2 = game.players[1]
    mask = Game.display_mask(game.mask)
    print(f"""
***************************************
Word:   {mask}
***************************************
Player: {p1.name}
{Img.get_image(p1.score)}
Wrong:  {p1.bad_choices}
---------------------------------------
Player: {p2.name}
{Img.get_image(p2.score)}
Wrong:  {p2.bad_choices}
***************************************
    """)
    input("Press Enter to continue: ")
    t.sleep(1)
    return transition_code


def turn(player, mask):
    # transition loop
    t_code = 0
    while t_code == 0:
        Tl.clear()
        player.turn(mask)
        t_code = player.valid_guess()
        t.sleep(1)


def you_lose(name):
    death_loop()
    t.sleep(1)
    print(f"""
***************************************
Player: {name} 
You lose!
***************************************""")


def you_win(name):
    win_loop()
    t.sleep(1)
    print(f"""
***************************************
Player: {name} 
You Win!
***************************************""")


def ending(players):
    for player in players:
        if player.lose == 1:
            you_lose(player.name)
        if player.win == 1:
            you_win(player.name)
    input("Press Enter to continue: ")


def end():
    Tl.end()


def win_loop():
    Tl.clear()
    print(Img.get_image(6))
    t.sleep(1)
    Tl.clear()
    print(Img.get_image(10))
    t.sleep(1)
    Tl.clear()
    print(Img.get_image(11))
    t.sleep(1)
    Tl.clear()
    print(Img.get_image(12))
    t.sleep(1)
    Tl.clear()
    print(Img.get_image(13))
    t.sleep(1)
    for i in range(2):
        Tl.clear()
        print(Img.get_image(14))
        t.sleep(1)
        Tl.clear()
        print(Img.get_image(15))
        t.sleep(1)


def death_loop():
    Tl.clear()
    print(Img.get_image(6))
    t.sleep(1)
    for i in range(2):
        Tl.clear()
        print(Img.get_image(7))
        t.sleep(1)
        Tl.clear()
        print(Img.get_image(8))
        t.sleep(1)
        Tl.clear()
        print(Img.get_image(7))
        t.sleep(1)
        Tl.clear()
        print(Img.get_image(9))
        t.sleep(1)
