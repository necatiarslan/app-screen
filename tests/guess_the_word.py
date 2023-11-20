import sys, os
sys.path.append(os.path.abspath("."))

from appscreen.window import Window
from appscreen.textbox import TextBox
from appscreen.label import Label
from appscreen.component import TextAlign
from appscreen.sound import beep

import random
from faker import Faker

class GuessTheWord(Window):

    letter_textbox = TextBox("letter_textbox")
    word_label = Label("word_label")
    info_label = Label("info_label")
    guessed_label = Label("guessed_label")
    caption_label = Label("caption_label")


    word_type = "STATE"
    guessed_letters = []
    attempts:int = 6
    word_to_guess:str

    def __init__(self, design_file_path):
        super().__init__(design_file_path)
        
        self.init_components()
    
    def init_components(self):
        self.word_label.text_align = TextAlign.Center

        self.letter_textbox.on_text_entered = self.letter_textbox_text_entered

        self.info_label.text_align = TextAlign.Center
        self.info_label.text = "Enter Your Guess"

        self.guessed_label.text_align = TextAlign.Right

        self.caption_label.text_align = TextAlign.Center

        self.add_component(self.letter_textbox)
        self.add_component(self.word_label)
        self.add_component(self.info_label)
        self.add_component(self.guessed_label)
        self.add_component(self.caption_label)

    def loaded(self):
        if self.word_type == "STATE":
            self.word_to_guess = Faker().state()
        elif self.word_type == "NAME":
            self.word_to_guess = Faker().first_name()
        elif self.word_type == "COUNTRY":
            self.word_to_guess = Faker().country()

        self.caption_label.text = "GUESS THE " + self.word_type
        self.word_label.text = self.get_word_display()
        self.letter_textbox.focus()
    
    def letter_textbox_text_entered(self):
        if self.letter_textbox.text_entered == "!":
            return
        
        re_focus = True

        guess = self.letter_textbox.text_entered

        if guess.isalpha() and len(guess) == 1:
            if guess in self.guessed_letters:
                self.info_label.text = "You already guessed that letter. Try again."
            elif guess in self.word_to_guess:
                self.guessed_letters.append(guess)
                self.info_label.text = "Good guess!"
                beep()
            else:
                self.guessed_letters.append(guess)
                self.attempts -= 1
                self.info_label.text = f"Wrong guess! Attempts left: {self.attempts}"
                if self.attempts == 0:
                    self.info_label.text =f"Sorry, you're out of attempts. It was {self.word_to_guess}."
                    re_focus = False

            
            self.guessed_label.text = ",".join(self.guessed_letters)
            self.word_label.text = self.get_word_display()


            if "_" not in self.word_label.text:
                self.info_label.text = "Congratulations :-)"
                re_focus = False

        else:
            self.info_label.text = "Invalid input. Please enter a single letter."

        if re_focus:
            self.letter_textbox.focus()

    def get_word_display(self):
        display = ""
        for letter in self.word_to_guess:
            if letter.lower() in self.guessed_letters:
                display += letter
            else:
                display += "_"
        return display

