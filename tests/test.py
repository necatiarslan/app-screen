import sys, os
sys.path.append(os.path.abspath("."))

from tests.guess_the_number import GuessTheNumber
from tests.guess_the_word import GuessTheWord
from tests.game_main_menu import GameMainMenu
from appscreen.color import Color

#window = GuessTheNumber("tests/guess_the_number.txt")
#window.debug_mode = True
#window.show()

selected_option = -1
while selected_option != 0:
    window = GameMainMenu("tests/game_main_menu.txt")
    window.fore_color = Color.Blue
    #window.debug_mode = True
    window.show()
    selected_option = window.selected_option

    if selected_option == 1:
        frm = GuessTheNumber("tests/guess_the_number.txt")
        frm.press_key_to_exit = True
        frm.show()
    elif selected_option == 2:
        theword = GuessTheWord("tests/guess_the_word.txt")
        theword.word_type = "STATE"
        theword.press_key_to_exit = True
        theword.show()
    elif selected_option == 3:
        theword = GuessTheWord("tests/guess_the_word.txt")
        theword.word_type = "COUNTRY"
        theword.press_key_to_exit = True
        theword.show()
    elif selected_option == 4:
        theword = GuessTheWord("tests/guess_the_word.txt")
        theword.word_type = "NAME"
        theword.press_key_to_exit = True
        theword.show()