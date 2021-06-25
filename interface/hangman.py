""" hangaman class with all methods"""

from random import randint
from unidecode import unidecode
import ascii_art
import os

class Hangman:


    def __init__(self):

        """ Define the principal status of the hangman
        """

        # Define the word
        self._word, self.duplicate, self.random_word = self._get_word()

        #The body for the hangman
        self.body = ascii_art.hangman_body()

        self.status = self.body[0]


    def _get_word(self):

        """ Gets the random word , and convert it in a dict.
        """

        with open("interface/assets/data.txt","r", encoding="utf-8") as f:

            # Obtain a list with the words
            w_list = [word for word in f if word != "\n"]
            #get a word
            self.random_word = unidecode(w_list[randint(1,len(w_list))])
            # Define the dict
            self._word = [{letter :"__"} for letter in self.random_word if letter != "\n"]
            self.duplicate = [{letter : letter } for letter in self.random_word if letter != "\n"]
            return (self._word, self.duplicate, self.random_word)


    def confirm(self, letter: str) :
        
        """ Confirms the existence of the letter in the dict, if the letter is in the dict, twist the position, key value.
        """

        #Confirm

        for i in range(len(self._word)):

            if letter in self._word[i].keys():

                self._word[i].update({letter : letter})
                os.system("clear")
                print("Muy bien, adivinaste\n")
                return 0
            else:
                continue

        os.system("clear")
        print("Lo siento no has adivinado\n")
        return 0

        





    