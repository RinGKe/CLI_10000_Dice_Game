import time

from dice import Dice


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


def test_multi_roll(nums=[]) -> None:
    dice = Dice("CPU")
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
    while data:
        time.sleep(1)
        roll = dice.roll_dice()
        if len(roll) == 6:
            print("=======================")
            print(f"Cup: {dice.cup_num}")
        print()
        print(roll)
        data = dice.check_selection(roll)
        for k, v in data.items():
            print(f"{k}: {v}")
        print("-----------------------")
        print(f"Score: {dice.current_score}")
        print("=======================")
    print("BUST")
    print("-----------------------")
    print(dice)


test_multi_roll()

"""
test_combos([1, 2, 3, 4, 5, 6])
test_combos([4, 4, 4, 6, 6, 6])
test_combos([2, 2, 3, 3, 4, 4])
test_combos([1, 1, 1, 1, 1, 1])
test_combos([2, 3, 4, 6, 2, 4])
test_combos()
"""
