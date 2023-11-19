import sys, os
sys.path.append(os.path.abspath("."))

from tests.guess_the_number import GuessTheNumber

window = GuessTheNumber("tests/guess_the_number.txt")
window.show()