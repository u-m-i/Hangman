import os
from random import randint, randrange
from unidecode import unidecode

def get_word():

    """ Gets the random word 
    """

    with open("words/data.txt","r", encoding="utf-8") as f:

        w_list = [word for word in f if word != '\n']
        random_word = unidecode(w_list[randint(1,len(w_list))])
        word_l = [ {letter.upper(): "__" } for letter in random_word if letter != "\n"]        

    return word_l


def confirm(letter: str, word: list):

    """ Confirms the existence of the letter in the list 
    """
    i_ = 0

    for i in range(len(word)):
        try:
            if letter in word[i].keys():
                i_ += 1  
                word.insert(i, str(letter))
                word.remove({letter: "__"})
            
            else:
                continue
    
        except AttributeError:
            return True

    if i_ > 0 :
        return word
    else:
        return print(f" {letter} no está dentro de la palabra")



def hangman_ascii():

    """ Store a constant with the hangman parts
    """

    HANGMANPICS = ['''
  +---+
      |
      |
      |
      |
      |
=========''',
        '''
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



def console():

    """ The console game
    """
    
    i = 0
    random_word = get_word()
    incognite = "__ "*len(random_word)

    print("##"*65, end="\n")
    print(f" Adivina la palabra de {len(random_word)} letras de largo.\n")
    print(incognite)

    user_letter = input("\nEscribe la letra que piensas: ").upper()
    assert user_letter.isnumeric() == False, "No hay ninguna palabra con números"

    confirm(user_letter, random_word)

    while i == 0:

        for j in random_word:
            try:
                incognite = incognite + " " + j.values()
            except AttributeError:
                incognite = incognite + " " + j


        print("##"*65, end="\n")
        
        user_letter = input("\nEscribe la letra que piensas: ").upper()
        assert user_letter.isnumeric() == False, "No hay ninguna palabra con números"

        print(confirm(user_letter, random_word))
        
        


def run():
    """ Start the game with a greeting
    """

    #Greeting and rules

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

    #The start part

    print("Okay Empecemos con tu primera palabra")
    console()


def test():
    pass
    

if __name__ == '__main__':
    test()