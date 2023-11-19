import sys, os
sys.path.append(os.path.abspath("."))

from appscreen.window import Window
from appscreen.textbox import TextBox
from appscreen.label import Label

window = Window("tests/ui_design.txt")

name_textbox = TextBox("name_textbox")
window.add_component(name_textbox)

name_label = Label("name_label")
name_label.text = "HELLO"
window.add_component(name_label)

window.show()