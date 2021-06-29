# This script contains all the Top-Level states


# start of program
from Game import Game
from os import system, name


def menu_answer_checker(answer):
    if answer == "1" or answer == "2" or answer == "3":
        return int(answer)

    print("\tInput Error: Please enter 1,2 or 3")
    return 0


# one player game
def one_player():
    print("\n\tone player")
    game = Game([])
    return game


# two players game
def two_players():
    print("\n\tTwo players")
    game = Game([])
    return game


# exiting game
def end():
    clear()
    print("""
Thank you for enjoying hangman!
Hope you had as much fun playing this version of hangman
as I enjoyed coding it. Goodbye!
""")
    input("Press Enter to exit!")
    clear()


# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
