""" The console to interact with """
# Hangman
from hangman import Hangman
from ascii_art import greeting
# Utilities
from time import sleep
import os


def interface(user_word, unknow_w, hangman):

    if user_word == unknow_w:
        know_w = ""
        for i in unknow_w:
            know_w = know_w + i

        print(f"\nLa palabra era: {know_w}")
        return "Felicidades! has completado la palabra"

    print("ª"*100,end="\n")
    print(f"La palabra està conformada por {len(user_word)} letras \n")

    for i in user_word:
        print(i, end=" ")

    user_letter= input("\nAhora adivina y danos una sola letra: ").upper()
    correct = hangman.confirm(user_letter)

    if True in correct:
        os.system("clear")
        print(correct[1])
        user_word = correct[2]
        return user_word, unknow_w

    elif correct is str:

        print(correct)
        
    else:

        print(correct[1])
        return user_word, unknow_w
        


def console():

    """ The console game
    """
    hangman = Hangman()
    user_word = hangman.incognite
    unknow_w = hangman._word

    

    greeting()
    user_word, unknow_w = interface(user_word, unknow_w, hangman)
    while user_word != unknow_w:
        user_word, unknow_w = interface(user_word, unknow_w, hangman)
    print(f"muy bien has ganado.")


    

if __name__ == "__main__":
    console()
  
    
    


   
    



