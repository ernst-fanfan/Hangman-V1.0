# Hangman program
# Author: Ernst Fanfan
# date: 06/23/2021
# AI object
import random as rn


class ArtificialLogic:
    def __init__(self):
        lst = []
        with open("./files/words.txt") as file:
            data = file.readlines()
            for line in data:
                word = line.split()
                lst += word
        self.words = []
        for w in lst:
            self.words.append([w, len(w)])
        self.letters = []
        self.empty = []

    def isolate(self, mask):
        lst = []
        for word in self.words:
            if word[1] == len(mask):
                lst.append(word[0])
        self.words = lst

    def analyze(self, mask):
        index = 0
        letters = []
        empty = []
        for letter in mask:
            if letter.isalpha():
                letters.append([letter, index])
            else:
                empty.append(index)
            index += 1
        self.letters = letters
        self.empty = empty

    def triage(self):
        lst = []
        for word in self.words:
            if self.is_word_good(word):
                lst.append(word)
        self.words = lst

    def is_word_good(self, word):
        for letter in self.letters:
            if letter[0] != word[letter[1]]:
                return False
        return True

    def pick(self, mask):
        self.analyze(mask)
        self.triage()
        i = rn.randint(0, len(self.words)-1)
        word = self.words[i]
        i = rn.randint(0, len(self.empty)-1)
        index = self.empty[i]
        return word[index]
