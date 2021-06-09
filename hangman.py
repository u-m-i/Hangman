import os
from random import randint
from unidecode import unidecode

def get_word():
    """ Gets the random word 
    """
    with open("words/data.txt","r", encoding="utf-8") as f:
        w_list = [word for word in f if word != "\n"]
        random_word = unidecode(w_list[randint(len(w_list))])
        w_dict = {letter.capitalize() : "__" for letter in random_word }


def hangman_ascii():
    HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def run():
    """ Start the game
    """
    print("""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/      
    """)
    print("==="*40)
    print("                                                       ¡ BIENVENIDO !                                                   \n")

    print("Las reglas son muy simples, se generará una palabra aleatoria y se te pedirá que adivines letra por letra. Cuando adivines, automáticamente se revelarán las letras en la palabra.")


if __name__ == '__main__':
    run()