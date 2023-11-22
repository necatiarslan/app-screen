from .color import Color
from enum import Enum

class TextAlign(Enum):
    Left = 1
    Center = 2
    Right = 3

class Component:
    window = None
    name = None
    x = None
    y = None
    width = None
    fore_color = None | Color
    back_color = None | Color
    
    @property
    def end(self):
        return self.x + self.width
    
    def to_string(self):
        return f"component:{self.name}, x={self.x}, y={self.y}, width={self.width}, end={self.end}"
    
    def draw(self):
        if self.window and self.window.stdscr and self.x and self.y:
            stdscr = self.window.stdscr
            stdscr.stdscr.addstr(self.y, self.x, f"[{self.name}]")
            stdscr.refresh()