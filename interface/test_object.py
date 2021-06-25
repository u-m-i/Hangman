import unittest
from hangman import Hangman
from console import interface


class HangmanTest(unittest.TestCase):

    def setUp(self) -> None:
        
        self.hang_man = Hangman()
        self.user_word = self.hang_man._word
        self.unknow = self.hang_man.incognite
        print(f"The word is : {self.hang_man._word}")

    def test_confirm(self):
        user_letter = input("letter: ")
        user_word = self.user_word
        unknow = self.unknow
        while self.user_word != self.unknow:

            interface(self.hang_man, user_word, unknow)
            self.asserTrue(user_word == unknow)


    def tearDown(self) -> None:
        print(f"The incognite: {self.hang_man.incognite}")


if __name__ == "__main__":
    unittest.main(verbosity=2)