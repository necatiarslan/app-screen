from .component import Component
from curses.textpad import Textbox as CursesTextBox
import curses

class TextBox(Component):
    """
    Control-A
    Go to left edge of window.

    Control-B
    Cursor left, wrapping to previous line if appropriate.

    Control-D
    Delete character under cursor.

    Control-E
    Go to right edge (stripspaces off) or end of line (stripspaces on).

    Control-F
    Cursor right, wrapping to next line when appropriate.

    Control-G
    Terminate, returning the window contents.

    Control-H
    Delete character backward.

    Control-J
    Terminate if the window is 1 line, otherwise insert newline.

    Control-K
    If line is blank, delete it, otherwise clear to end of line.

    Control-L
    Refresh screen.

    Control-N
    Cursor down; move down one line.

    Control-O
    Insert a blank line at cursor location.

    Control-P
    Cursor up; move up one line.
    """
    curses_textbox = None
    on_text_entered = None
    text_entered:str = ""

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
                self.curses_textbox = CursesTextBox(win,insert_mode=True)
            
    def focus(self):
        if self.curses_textbox:
            self.text_entered = self.curses_textbox.edit()
            self.text_entered = self.text_entered.strip() #clear spaces
            if self.on_text_entered:
                self.on_text_entered()

