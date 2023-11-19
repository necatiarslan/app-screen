from .component import Component

class TextBox(Component):
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
            stdscr.addstr(self.y, self.x, f"<{self.name}>")
