from collections import Counter
from enum import Enum

from cli_throbber import CLI_Throbber


class Combo(Enum):
    DOUBLE_TRIPS = 2500
    LARGE_STRAIGHT = 1500
    SIX_KIND = 800
    FIVE_KIND = 400
    FOUR_KIND = 200
    THREE_PAIRS = 500
    THREE_KIND = 100
    NONE = 0


class Dice:
    def __init__(self, amount=6) -> None:
        self.amount = amount
        self.active_dice = 6
        self.num_rolls = 0
        self.cup_num = 0
        self.current_score = 0
