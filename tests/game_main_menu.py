import sys, os
sys.path.append(os.path.abspath("."))

from appscreen.window import Window
from appscreen.textbox import TextBox
from appscreen.label import Label
from appscreen.component import TextAlign

import random

class GameMainMenu(Window):

    option_textbox = TextBox("option_textbox")
    selected_option:int

    def __init__(self, design_file_path):
        super().__init__(design_file_path)
        
        self.init_components()
    
    def init_components(self):

        self.option_textbox.on_text_entered = self.option_textbox_text_entered

        self.add_component(self.option_textbox)

    def loaded(self):
        self.option_textbox.focus()
    
    def option_textbox_text_entered(self):
        re_focus = True
        if self.option_textbox.text_entered.isnumeric():
            self.selected_option = int(self.option_textbox.text_entered)
            re_focus = False
            
        if re_focus:
            self.option_textbox.focus()
        