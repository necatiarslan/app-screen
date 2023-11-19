from .component import Component, TextAlign

class Label(Component):
    text = None
    text_align:TextAlign = None

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
        if self.window and self.window.stdscr and self.text and self.x and self.y:
            stdscr = self.window.stdscr
            stdscr.addstr(self.y, self.x, self.draw_text())
    
    def draw_text(self):
        result = ""
        if self.text_align == TextAlign.Center:
            left_space = " " * ((self.width - len(self.text)) // 2)
            right_space = " " * (self.width - len(left_space) - len(self.text))
            result = left_space + self.text + right_space
        elif self.text_align == TextAlign.Right:
            left_space = " " * (self.width - len(self.text))
            result = left_space + self.text
        else: #none or left
            right_space = " " * (self.width - len(self.text))
            result = self.text + right_space
        return result