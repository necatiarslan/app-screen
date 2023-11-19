import sys, os
sys.path.append(os.path.abspath("."))

from tests.guess_the_number import GuessTheNumber
from tests.guess_the_word import GuessTheWord
from tests.game_main_menu import GameMainMenu

#window = GuessTheNumber("tests/guess_the_number.txt")
#window.debug_mode = True
#window.show()

selected_option = -1
while selected_option != 0:
    window = GameMainMenu("tests/game_main_menu.txt")
    #window.debug_mode = True
    window.show()
    selected_option = window.selected_option

    if selected_option == 1:
        GuessTheNumber("tests/guess_the_number.txt").show()
    elif selected_option == 2:
        theword = GuessTheWord("tests/guess_the_word.txt")
        theword.word_type = "STATE"
        theword.show()
    elif selected_option == 3:
        theword = GuessTheWord("tests/guess_the_word.txt")
        theword.word_type = "COUNTRY"
        theword.show()
    elif selected_option == 4:
        theword = GuessTheWord("tests/guess_the_word.txt")
        theword.word_type = "NAME"
        theword.show()