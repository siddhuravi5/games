import random
import time
import sys


class hangman:


    _hangman = (
    """
    """,
    """
    ---
    |
    ---
    """,
    """
    ----
    |  |
    ----
    """,
    """
    ---- |   |
    |  | |   |
    ---- |___|
    """,
    """
    ---- |   | -----
    |  | |   |   |
    ---- |___|   |
    """)


    def __init__(self):
        wordsa = ["hello", "world"]
        self.worda = random.choice(wordsa)
        self.used = []
        self.sofar = ("_ " * len(self.worda)).strip()
        self.word = ""
        for i in self.worda:
            self.word = self.word + i + " "
        self.word = (self.word).strip()


    def play(self):
        self.__init__()
        print("come on , lets play")

        self.life = 4
        self.game()


    def game(self):
        print (self.sofar)
        time.sleep(1)
        print("lives remaining: ", self.life)
        time.sleep(1)
        print(self._hangman[4 - self.life])
        time.sleep(1)
        print("letters so far used: ", self.used)
        time.sleep(1)
        print()
        print()
        print()
        if self.sofar.strip() != self.word.strip() and self.life != 0:
            inp = input("guess some letter : ")
        if self.sofar.strip() != self.word.strip() and self.life != 0:
            if inp in self.word and inp not in self.used:
                new = ""
                for i in range(0, len(self.sofar), 2):

                    if inp == self.word[i]:
                        print("good")
                        time.sleep(1)
                        new = new + (self.word[i] + " ")
                    else:
                        new = new + (self.sofar[i] + " ")
                self.sofar = new

            elif inp in self.used:
                print(" letter already used")
                self.game()
            else:
                print("not present")
                self.life -= 1

        elif self.life == 0:
            print(self._hangman[4 - self.life])
            print("you lose")
            print("answer is: ", self.word)
            sys.exit()
        else:
            print ("the word is ",end="")
            print (self.sofar)
            print ("very good")
            print("winner")
            sys.exit()
        self.used.append(inp)
        self.game()


gamer = hangman()
gamer.play()

