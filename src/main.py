from cli_throbber import CLI_Throbber
from dice import Dice

roll_throbber = CLI_Throbber("Press 'ENTER' to Roll...")
player_dice = Dice("Player")


def main():
    roll_throbber.start()
    while True:
        key = input()
        if key == "" or key != "":
            roll_throbber.stop()
            break
    roll = player_dice.roll_dice()
    print(roll)
    data = player_dice.check_selection(roll)
    for k, v in data.items():
        print(f"{k}: {v}")
    print("-----------------------")
    print(f"Score: {player_dice.current_score}")


if __name__ == "__main__":
    main()
