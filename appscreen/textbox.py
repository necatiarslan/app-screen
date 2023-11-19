from .component import Component
from curses.textpad import Textbox as CursesTextBox
import curses

class TextBox(Component):
    curses_textbox = None

    def __init__(self, name, **kwargs):
        self.name = name
        for k, v in kwargs.items():
            if k == "x":
                self.x = v
            if k == "y":
                self.y = v

            if k == "width":
                self.width = v

    def draw(self):
        if self.window and self.window.stdscr and self.x and self.y:
            stdscr = self.window.stdscr
            if not self.curses_textbox:
                win = curses.newwin(1, self.width, self.y, self.x)
                self.curses_textbox = CursesTextBox(win)
                
            
    def focus(self):
        if self.curses_textbox:
            self.curses_textbox.edit()