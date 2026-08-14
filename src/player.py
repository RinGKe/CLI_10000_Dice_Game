import random
import time

from .cli_throbber import CLI_Throbber
from .dice import Dice


class Player:
    def __init__(self, name: str = "", threshold: int = 0):
        self.name = name
        self.threshold = threshold
        self.score = 0
        self.isThreshold = False

    def play_turn(self, speed: float):
        dice = Dice(self.name)
        while True:
            roll = dice.roll_dice()
            if len(roll) == 6:
                print("===========================\\\\\\")
                print(f"                    Cup: {dice.cup_num}")

            roll_bar = CLI_Throbber(f"Rolling {dice.active_dice}...", time=(speed * 2))
            roll_bar.start()
            print()

            print(roll)

            user_input = [
                int(x) for x in input("Select dice to keep... :\n") if x.isdigit()
            ]
            roll_copy = roll.copy()
            selection = []
            for c in user_input:
                if c in roll_copy:
                    selection.append(int(c))
                    roll_copy.remove(int(c))
            if not selection:
                selection = roll
            print("\033[F\033[K", end="\r")
            print("\033[F\033[K", end="\r")
            print(f"Held: {selection}")

            data = dice.check_selection(selection)
            if not data:
                time.sleep(speed / 2)
                print("=========================")
                print("<><><><><><><><><> <><><> <><>")
                print(f" BUST   {dice.current_score}")
                print("<><><><> <><><>  <><")
                self.score += 0
                break

            for k, v in data.items():
                time.sleep(speed)
                print(f"  * {k}: {v}")
            time.sleep(speed)
            print("------------------------")
            time.sleep(speed)
            print(f"Rolling Score: {dice.current_score}")
            print(f"Dice to roll:  {dice.active_dice}")
            print("=========================")

            if not self.isThreshold and (dice.current_score < self.threshold):
                if dice.current_score >= self.threshold or self.score >= self.threshold:
                    self.isThreshold = True
                else:
                    print(
                        f"* Need '{self.threshold - dice.current_score}' more points! *"
                    )
                    roll_throb = CLI_Throbber(
                        f"ENTER to roll {dice.active_dice}",
                        erase=True,
                    )
                    roll_throb.start()
                    entered = input()
                    roll_throb.stop()
                    continue

            roll_throb = CLI_Throbber(f"Roll {dice.active_dice}? (Y/N)", erase=True)
            roll_throb.start()
            entered = input()
            while entered not in ("y", "n", ""):
                print("\033[F\033[K", end="\r")
                _ = input()

            if entered == "y" or entered == "":
                roll_throb.stop()

            elif entered == "n":
                roll_throb.stop()
                print("<><><><><><><><><><><><><><><>")
                print(
                    f" SCORED  {dice.current_score}  ->  {dice.current_score + self.score}"
                )
                print("<><><><><><><><><><><><><><><>")
                self.score += dice.current_score
                break


class CPU(Player):
    def cpu_choice(self, dice: Dice) -> float:
        if not self.isThreshold:
            if dice.current_score < self.threshold:
                return 1.0
            else:
                self.isThreshold = True
                return -1.0
        if dice.active_dice == 6:
            return 1.0
        return dice.active_dice / (dice.amount - len(dice.addons))

    def play_turn(self, speed: float):
        dice = Dice(self.name)
        while True:
            roll = dice.roll_dice()
            if len(roll) == 6:
                print("===========================\\\\\\")
                print(f"                    Cup: {dice.cup_num}")

            roll_bar = CLI_Throbber(f"Rolling {dice.active_dice}...", time=(speed))
            roll_bar.start()
            print()

            print(roll)
            data = dice.check_selection(roll)
            if not data:
                time.sleep(speed / 2)
                print("=========================")
                print("<><><><><><><><><> <><><> <><>")
                print(f" BUST   {dice.current_score}")
                print("<><><><> <><><>  <><")
                self.score += 0
                break

            time.sleep(speed)

            for k, v in data.items():
                print(f"  * {k}: {v}")
            print("------------------------")

            time.sleep(speed / 2)

            print(f"Rolling Score: {dice.current_score}")
            print(f"Dice to roll:  {dice.active_dice}")
            print("=========================")

            time.sleep(speed * 2)

            if random.random() > self.cpu_choice(dice):
                print("<><><><><><><><><><><><><><><>")
                print(
                    f" SCORED  {dice.current_score}  ->  {dice.current_score + self.score}"
                )
                print("<><><><><><><><><><><><><><><>")
                self.score += dice.current_score
                break
