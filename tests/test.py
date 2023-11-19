import sys, os
sys.path.append(os.path.abspath("."))

from appscreen.window import Window
from appscreen.textbox import TextBox
from appscreen.label import Label
from tests.guess_the_number import GuessTheNumber

design_path = "tests/guess_the_number.txt"

window = GuessTheNumber(design_path)
window.show()