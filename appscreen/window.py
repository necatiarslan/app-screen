import curses
import re
from .label import Label
from .textbox import TextBox
from .color import Color

class Window():
    components:{} = {}
    design:str = None
    stdscr = None
    show_cursor:bool = True
    text_color:None | Color
    back_color:None | Color
    debug_mode:bool = False
    press_key_to_exit:bool = False

    def __init__(self, design_file_path):
        with open(design_file_path, 'r') as file:
            self.design = file.read()

    @staticmethod
    def main(stdscr, window):
        window.stdscr = stdscr
        window.draw()
        window.loaded()
        
        #window is closing
        window.before_closing()

        if window.press_key_to_exit:
            window.stdscr.getch()

    def show(self):
        self.get_ui_components()
        curses.wrapper(Window.main, self)

    def add_component(self, component):
        c = self.get_component(component.name)
        if c is None:
            self.components[component.name]= component
    
    def get_component(self, name):
        if name in self.components:
            return self.components[name]
        return None

    def get_ui_components(self):
        # Define a regex pattern to match {textbox:component_name} or {label:component_name}
        pattern = r'{(textbox|label):(\w+\s*)}'

        # Find all matches in the design
        matches = re.finditer(pattern, self.design)

        for match in matches:
            # Extract component type and name
            component_type, component_name = match.groups()

            line_number = self.design.count('\n', 0, match.start())
            line_start = self.design.rfind('\n', 0, match.start()) + 1
            column_number = match.start() - line_start
            width = match.end() - match.start()

            component_name = component_name.strip()
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
        
        #clear component texts
        lines = self.design.split('\n')
        cleared_design = ""
        for y, line in enumerate(lines):
            for c in self.components.values():
                if c.y == y:
                    line = line[:c.x] + (" " * c.width) + line[c.end:]
            cleared_design += line + "\n"
        
        self.design = cleared_design

    def get_dimentions(self):
        if self.stdscr:
            height, width = self.stdscr.getmaxyx()
            return height, width

    def draw(self):
        self.stdscr.clear()
        self.stdscr.refresh()

        if self.show_cursor:
            curses.curs_set(2)
        else:
            curses.curs_set(0)

        lines = self.design.split('\n')
        for y, line in enumerate(lines):
            self.stdscr.addstr(y, 0, line)
        
        self.draw_components()
        self.draw_debug()

        self.stdscr.refresh()

    def draw_components(self, component=None):
        if component:
            component.draw()
        else:
            for c in self.components.values():
                c.draw()

    def draw_debug(self):
        if self.debug_mode:
            for c in self.components.values():
                y += 1
                self.stdscr.addstr(y, 0, c.to_string())

    def loaded(self):
        pass #handle in the window itself
    
    def before_closing(self):
        pass #handle in the window itself