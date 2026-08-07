import random
from collections import Counter
from enum import Enum

from cli_throbber import CLI_Throbber
from scoring import eval_dice, score_dice


class Dice:
    def __init__(self, name: str, amount=6) -> None:
        self.name = name
        self.amount = amount
        self.active_dice = amount
        self.cup_num = 0
        self.current_score = 0

    def roll_dice(self) -> list[int]:
        roll = [random.randint(1, 6) for i in range(self.active_dice)]
        if self.active_dice == 6:
            self.cup_num += 1
        return roll

    def check_selection(self, given_dice: list[int]) -> dict[str, int]:
        self.current_score, remaining, data = score_dice(given_dice)
        self.active_dice = self.active_dice - (len(given_dice) - len(remaining))
        return data

    def __repr__(self) -> str:
        return f"""
        ---------------------------------
        {self.name}'s Dice
        Rolling Score: {self.current_score}
        Dice to Roll: {self.active_dice}/{self.amount}
        Cup Number: {self.cup_num}
        ---------------------------------
        """
