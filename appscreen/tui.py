import curses
import re
from enum import Enum

class Color(Enum):
    Black = curses.COLOR_BLACK
    White =  curses.COLOR_WHITE
    Blue =  curses.COLOR_BLUE
    Cyan = curses.COLOR_CYAN
    Green = curses.COLOR_GREEN
    Magenta = curses.COLOR_MAGENTA
    Red = curses.COLOR_RED
    Yellow = curses.COLOR_YELLOW

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

class Label(Component):
    text = None
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
            stdscr.addstr(self.y, self.x, self.text)

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

class Window():
    components = []
    design = None
    stdscr = None

    def __init__(self, design_file_path):
        with open(design_file_path, 'r') as file:
            self.design = file.read()

    @staticmethod
    def main(stdscr, window):
        window.stdscr = stdscr
        window.draw()

    def show(self):
        self.get_ui_components()
        curses.wrapper(Window.main, self)

    def add_component(self, component):
        c = self.get_component(component.name)
        if c is None:
            self.components.append(component)
    
    def get_component(self, name):
        for c in self.components:
            if c.name == name:
                return c
        return None

    def get_ui_components(self):
        # Define a regex pattern to match {textbox:component_name} or {label:component_name}
        pattern = r'{(textbox|label):(\w+)}'

        # Find all matches in the design
        matches = re.finditer(pattern, self.design)

        for match in matches:
            # Extract component type and name
            component_type, component_name = match.groups()

            line_number = self.design.count('\n', 0, match.start())
            line_start = self.design.rfind('\n', 0, match.start()) + 1
            column_number = match.start() - line_start
            width = match.end() - match.start()

            c = self.get_component(component_name)
            if c is None:
                if component_type == "textbox":
                    text_box = TextBox(component_name, x=column_number, y=line_number, width=width)
                    text_box.window = self
                    self.add_component(text_box)
                elif component_type == "label":
                    label = Label(component_name, x=column_number, y=line_number, width=width)
                    label.window = self
                    self.add_component(label)
            else:
                c.x = column_number
                c.y = line_number
                c.width = width
                c.window = self

    def draw(self):
        stdscr = self.stdscr
        curses.curs_set(0)
        stdscr.clear()
        stdscr.refresh()

        # Get screen dimensions
        # height, width = stdscr.getmaxyx()

        lines = self.design.split('\n')
        for y, line in enumerate(lines):
            for c in self.components:
                if c.y == y:
                    line = line[:c.x] + (" " * c.width) + line[c.end:]

            stdscr.addstr(y, 0, line)
        
        for c in self.components:
            c.draw()
        
        stdscr.getch()
    



