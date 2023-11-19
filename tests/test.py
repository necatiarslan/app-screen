import sys, os
sys.path.append(os.path.abspath("."))

from tests.guess_the_number import GuessTheNumber
from tests.guess_the_word import GuessTheWord

#window = GuessTheNumber("tests/guess_the_number.txt")
#window.debug_mode = True
#window.show()

window = GuessTheWord("tests/guess_the_word.txt")
#window.debug_mode = True
window.show()