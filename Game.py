# Hangman program
# Author: Ernst Fanfan
# date: 06/23/2021
# game object
import random as rn
from Ai import ArtificialLogic


def display_mask(mask):
    m_display = ""
    for spot in mask:
        m_display += spot + " "
    return m_display


class Game:

    def __init__(self, players):
        self.players = players
        self.word = ""
        self.word_picker()
        self.mask = []
        self.masker()
        self.end = False

    def update(self):
        # get stats amd mask for each player
        for player in self.players:
            self.mask = player.get_status(self.word, self.mask)
            if player.win == 1 or player.lose == 1:
                return 0
        return 1

    def word_picker(self):
        # file preparation
        with open("./files/words.txt") as file:
            lst = []
            data = file.readlines()
            for line in data:
                word = line.split()
                lst += word

        # picking random word
        index = rn.randrange(1, 854)
        self.word = lst[index]

    def masker(self):
        for _ in self.word:
            self.mask += "_"


class Player:

    def __init__(self, num, name):
        self.bad_choices = []
        self.good_choices = []
        self.current_choice = ""
        if num == 1:
            self.name = name
            self.score = 0
            self.win = 0
            self.lose = 0
            self.ai = 0
        if num == 0:
            self.name = name
            self.score = 0
            self.win = 0
            self.lose = 0
            self.ai = 1
            self.brain = ArtificialLogic()

    def get_status(self, word, mask):
        # update mask
        new_mask = self.update_status(word, mask)
        return new_mask

    def update_status(self, word, mask):
        index = 0
        found = 0
        if self.current_choice != "":
            # check if choice is in the word ands update mask
            for letter in word:
                if self.current_choice == letter:
                    # update mask
                    mask[index] = self.current_choice
                    found = 1
                index += 1
            # update good guesses
            if found == 1:
                self.good_choices += self.current_choice
            # update bad guesses
            if found == 0:
                self.bad_choices += self.current_choice
                self.score += 1

        # win or lose checker
        if self.score == 6:
            self.lose = 1
        if "_" not in mask:
            self.win = 1
        self.current_choice = ""

        return mask

    # player turn
    def turn(self, mask):

        if self.ai == 1:
            self.current_choice = self.brain.pick(mask)
        else:
            print(f"""
Player {self.name}'s Turn.
Word: {display_mask(mask)}
Wrong guesses: {self.bad_choices}
""")
            self.current_choice = input("Guess: ")

    # check if guess id a letter
    def valid_guess(self):
        if self.current_choice.isalpha():
            if self.current_choice in self.bad_choices or self.current_choice in self.good_choices:
                print(f"You picked {self.current_choice} already. Try again!")
            else:
                return 1

        print(f"{self.current_choice} is not a valid guess. Try again!")
        return 0
