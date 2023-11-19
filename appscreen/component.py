from .color import Color

class Component:
    window = None
    name = None
    x = None
    y = None
    width = None
    text_color = None | Color
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