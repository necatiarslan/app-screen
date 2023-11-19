import sys, os
sys.path.append(os.path.abspath("."))

from appscreen import tui

window = tui.Window("tests/ui_design.txt")

name_textbox = tui.TextBox("name_textbox")
window.add_component(name_textbox)

name_label = tui.Label("name_label")
name_label.text = "HELLO"
window.add_component(name_label)

window.show()