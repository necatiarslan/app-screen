import sys, os
sys.path.append(os.path.abspath("."))

from appscreen.window import Window
from appscreen.textbox import TextBox
from appscreen.label import Label
from appscreen.component import TextAlign

import random

class GuessTheNumber(Window):

    name_textbox = TextBox("name_textbox")
    name_label = Label("name_label")

    number = random.randint(1, 20)
    guess = None

    def __init__(self, design_file_path):
        super().__init__(design_file_path)
        
        self.init_components()
    
    def init_components(self):
        self.name_label.text_align = TextAlign.Center
        self.name_label.text = "Enter Your Guess"

        self.name_textbox.on_text_entered = self.name_textbox_text_entered

        self.add_component(self.name_textbox)
        self.add_component(self.name_label)

    def loaded(self):
        self.name_textbox.focus()
    
    def name_textbox_text_entered(self):
        if self.name_textbox.text_entered == "!":
            return

        re_focus = True
        if self.name_textbox.text_entered.isnumeric():
            guess = int(self.name_textbox.text_entered)
            if guess < self.number:
                self.name_label.text = "Too low!"
            elif guess > self.number:
                self.name_label.text = "Too high!"
            elif guess == self.number:
                self.name_label.text = "You win the game :-)"
                re_focus = False
        else:
            self.name_label.text = f"Please Enter a Number"
            
        if re_focus:
            self.name_textbox.focus()
        