""" hangaman class with all methods"""

from random import randint
from unidecode import unidecode
import ascii_art

class Hangman:


    def __init__(self) -> None:

        """ Define the principal status of the hangman
        """

        # Define the word
        self._word, self.incognite = self._get_word()

        #The body for the hangman
        self.body = ascii_art.hangman_body()

        self.status = self.body[0]


    def _get_word(self) -> tuple:

        """ Gets the random word , and convert it in a dict.
        """

        with open("console/assets/data.txt","r", encoding="utf-8") as f:

            # Obtain a list with the words
            w_list = [word for word in f if word != "\n"]
            #get a word
            random_word = unidecode(w_list[randint(1,len(w_list))])
            #
            self._word = [letter.upper() for letter in random_word if letter != "\n"]  
            self.incognite = ["__" for i in self._word ]

            return (self._word, self.incognite)


    def confirm(self, letter: str) -> tuple :
        
        """ Confirms the existence of the letter in the list. If the letter is correct, the incognite list gets replace the letter.
        """


        if self._word == self.incognite:

            return  "Lo lograste, completaste la palabra."

        else:

            for i in range(len(self._word)):

                if letter == self._word[i]:
                    
                    self.incognite.remove(self.incognite[i])
                    self.incognite.insert(i,letter)

                    return (True, "Le atinaste Muy bien!", self.incognite)
                    
                else:
                    continue

            else:

                return (False, "Lo lamento no has atinado")






    