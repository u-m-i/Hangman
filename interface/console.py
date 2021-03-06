""" The console to interact with """
# Hangman
from hangman import Hangman
from assets.ascii_art import greeting
# Utilities

import os
from time import sleep


class Console:

    
    def __init__(self) -> None:

        #Print the greeting()
        greeting()
        # Initialize the object
        self.hangman = Hangman()
        self.user_word = self.hangman._word
        self.duplicate = self.hangman.duplicate


    def interface(self):
        if self.duplicate == self.user_word:
            i = 1
            print("Felicidades, GANASTE!!!!")
            return i + 1

        print(f"La palabra tiene {len(self.user_word)} letras.\n")

        for i in range(len(self.user_word)):
            for j in self.user_word[i].values():
                print(f"{j} " , end=" ")
        
        print("\n")
        self.user_letter = input("Pon aquí tu letra: ")
        self.checkout(self.user_letter)
    

    def checkout(self,user_letter):
        self.hangman.confirm(user_letter)



def run():
    i = 0
    sleep(2)
    console_1 = Console()
    sleep(3)
    while i < 1:
        console_1.interface()


if __name__ == "__main__":
    run()
    




        
    




      
        
    


   
    



