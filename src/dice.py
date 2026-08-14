import random

from .scoring import score_dice


class Dice:
    def __init__(self, name: str, amount: int = 6):
        self.name = name
        self.amount = amount
        self.active_dice = amount
        self.cup_num = 0
        self.addons = {0}
        self.current_score = 0

    def roll_dice(self) -> list[int]:
        roll = [random.randint(1, 6) for _ in range(self.active_dice)]
        if self.active_dice == 6:
            self.cup_num += 1
            self.addons = {0}
        return roll

    def check_selection(self, given_dice: list[int]) -> dict[str, int]:
        if not given_dice:
            return {}
        points, remaining, new_addon, data = score_dice(given_dice, self.addons)
        self.current_score += points
        self.active_dice = self.active_dice - (len(given_dice) - len(remaining))
        self.active_dice = 6 if self.active_dice == 0 else self.active_dice
        self.addons.add(new_addon)
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
