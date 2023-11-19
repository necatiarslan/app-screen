import sys, os
sys.path.append(os.path.abspath("."))

from appscreen.window import Window
from appscreen.textbox import TextBox
from appscreen.label import Label
from appscreen.component import TextAlign

class GuessTheNumber(Window):

    name_textbox = TextBox("name_textbox")
    name_label = Label("name_label")

    def __init__(self, design_file_path):
        super().__init__(design_file_path)
        
        self.init_components()
    
    def init_components(self):
        self.name_label.text_align = TextAlign.Center
        self.name_label.text = "Enter Your Guess"

        self.add_component(self.name_textbox)
        self.add_component(self.name_label)