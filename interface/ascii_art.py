""" here are the ascci art
"""

def hangman_body() -> list:
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
    return HANGMANPICS


def greeting():

    """ Start the game with a greeting
    """
    with open("/home/umi/Documents/Projects/devs/Hangman/interface/assets/welcom.txt" , "r", encoding="utf-8") as f:
      print(f.read())


