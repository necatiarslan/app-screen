import curses
from enum import Enum

class Color(Enum):
    Black:int = curses.COLOR_BLACK
    White:int =  curses.COLOR_WHITE
    Blue:int =  curses.COLOR_BLUE
    Cyan:int = curses.COLOR_CYAN
    Green:int = curses.COLOR_GREEN
    Magenta:int = curses.COLOR_MAGENTA
    Red:int = curses.COLOR_RED
    Yellow:int = curses.COLOR_YELLOW

class ColorPair():
    pair_number = 0

def get_pair_number(fore_color:int | None, back_color:int | None) -> int:
    ColorPair.pair_number += 1
    
    if fore_color is None:
         fore_color = Color.White
    
    if back_color is None:
         back_color = Color.Black

    if isinstance(fore_color, Color):
         fore_color = fore_color.value
    
    if isinstance(back_color, Color):
         back_color = back_color.value

    curses.init_pair(ColorPair.pair_number, fore_color, back_color)
    return ColorPair.pair_number

def get_colors(pair_number:int):
        return curses.pair_content(pair_number)