import curses
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

pair_number = 0
def get_pair_number(fore_color:Color, back_color:Color) -> int:
    pair_number += 1
    curses.init_pair(pair_number, fore_color, back_color)
    return pair_number

def get_colors(pair_number:int):
        return curses.pair_content(pair_number)