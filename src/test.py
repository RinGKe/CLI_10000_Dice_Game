import time

from dice import Dice
from gamemode import Gamemode


def test_combos(nums=[]) -> None:
    dice = Dice("Player")
    roll = nums if nums else dice.roll_dice()
    print(roll)
    data = dice.check_selection(roll)
    if not data:
        print("BUST")
    for k, v in data.items():
        print(f"{k}: {v}")
    print("-----------------------")
    print(f"Score: {dice.current_score}")
    print("=======================")


def test_machine():
    total_rounds = 0
    iteration = 0
    total_score = 1000
    current_score = 0
    while True:
        iteration += 1
        total_rounds += 1
        current_score = test_multi_roll()
        total_score += current_score
        average = round(total_score / iteration)
        print(f"**** TARGET: {average} ****")
        print(f"**** ROUNDS: {total_rounds} ****")
        if current_score > 10000:
            break
        if iteration == 10:
            iteration = 0
            total_score = 1000
        time.sleep(0.5)


def test_multi_roll(nums=[]) -> int:
    dice = Dice("CPU")
    while True:
        time.sleep(0.1)
        roll = dice.roll_dice()
        if len(roll) == 6:
            print("=================================")
            print(f"Cup: {dice.cup_num}")
        print()
        print(roll)
        data = dice.check_selection(roll)
        if not data:
            break
        for k, v in data.items():
            print(f"{k}: {v}")
        print("-----------------------")
        print(f"Score: {dice.current_score}")
        print("=========================")
    print("BUST")
    print("-------------------------")
    print(dice)
    return dice.current_score


def test_round():
    gamemode = Gamemode(player_num=0, cpu_num=3)
    gamemode.run_round()
    gamemode.eval_top_score()


def test_multi_round(limit: int):
    gamemode = Gamemode(player_num=0, cpu_num=3)
    while True:
        gamemode.run_round()
        gamemode.eval_top_score()
        if gamemode.round >= limit:
            break


test_multi_round(3)

"""test_machine()"""

"""
test_combos([1, 2, 3, 4, 5, 6])
test_combos([4, 4, 4, 6, 6, 6])
test_combos([2, 2, 3, 3, 4, 4])
test_combos([1, 1, 1, 1, 1, 1])
test_combos([2, 3, 4, 6, 2, 4])
test_combos()
"""
