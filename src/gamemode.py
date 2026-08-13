import random
import time

from dice import Dice


class Gamemode:
    def __init__(self, player_num=1, cpu_num=1, win_score=10000, speed=1) -> None:
        self.win_score = win_score
        self.speed = speed
        self.round = 0
        self.winner = ("", 0)
        self.players = [[f"Player {x + 1}", 0] for x in range(player_num)] + [
            [f"CPU {x + 1}", 0] for x in range(cpu_num)
        ]

    def player_turn(self) -> int:
        return 0

    def cpu_turn(self, name: str) -> int:
        dice = Dice(name)
        turn_score = 0
        while True:
            roll = dice.roll_dice()
            if len(roll) == 6:
                print("==============================")
                print(f"Cup: {dice.cup_num}")
            print(f"Rolling {dice.active_dice}...")
            print()

            time.sleep(self.speed * 2)

            print(roll)
            data = dice.check_selection(roll)
            if not data:
                print("******************************")
                print(f"  BUST {dice.current_score}")
                print("******************************")
                return 0

            time.sleep(self.speed)

            for k, v in data.items():
                print(f" * {k}: {v}")
            print("------------------------")

            time.sleep(self.speed / 2)

            print(f"Rolling Score: {dice.current_score}")
            print("=========================")

            time.sleep(self.speed)

            if random.random() < 0.5:
                print("******************************")
                print(f"  SCORED {dice.current_score}")
                print("******************************")
                return dice.current_score

    def run_round(self) -> None:
        self.round += 1
        print()
        print()
        print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
        print(f"     ROUND {self.round}")
        print("////////////////////")
        for p in self.players:
            time.sleep(self.speed)
            print()
            print()
            print("//////////")
            print(f" {p[0]}")
            print("\\\\\\\\\\\\\\\\\\\\")
            time.sleep(self.speed)
            if "CPU" in p[0]:
                p[1] += self.cpu_turn(p[0])
            else:
                p[1] += self.player_turn()

    def eval_top_score(self) -> None:
        time.sleep(self.speed)
        places = sorted(self.players, key=lambda x: x[1], reverse=True)
        print()
        print("        ============================")
        print(f"         [Round {self.round} results]")
        for i, p in enumerate(places):
            print(f"          {i + 1}: {p[0]} -> {p[1]}")
        print("        ============================")
        if places[0][1] > self.win_score:
            self.winner = (places[0][0], places[0][1])
