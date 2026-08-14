import sys

from .gamemode import Gamemode

speed_defaults = {
    "slow": (1, 1),
    "normal": (0.5, 0.5),
    "fast": (0.125, 0.5),
    "hyper": (0.01, 0.1),
}


def create_gamemode() -> Gamemode:
    print("\033[F\033[K", end="\r")
    print()

    # use defaults settings?
    selection = input(
        "Use game setting defaults? (Players: 1, CPU: 1, Speed: normal) \n(Y/N): "
    )
    lines = 3
    while selection not in ("y", "n", ""):
        lines += 2
        selection = input(
            "Use game setting defaults? (Players: 1, CPU: 1, Speed: normal) \n(Y/N)"
        )
    if selection in ("y", ""):
        print(("\033[F\033[K") * lines, end="\r")
        return Gamemode(players=1, cpus=1, speed=0.5, pause=0.5)
    print(("\033[F\033[K") * lines, end="\r")

    # select player amount
    selection = input("How many players? (Default: 1)...\n")
    lines = 2
    while not selection.isdigit() and selection != "":
        lines += 2
        selection = input("How many players? (Default: 1)...\n")
    player_selection = int(selection) if selection else 1
    print(("\033[F\033[K") * lines, end="\r")
    print(f"Players: [{player_selection}]")

    # select cpu amount
    selection = input("How many computers opponents? (Default: 1)...\n")
    lines = 2
    while not selection.isdigit() and selection != "":
        lines += 2
        selection = input("How many computers opponents? (Default: 1)...\n")
    cpu_selection = int(selection) if selection else 1
    print(("\033[F\033[K") * lines, end="\r")
    print(f"CPUs: [{cpu_selection}]")

    # select speed
    selection = input(
        "Game speed? \n(Slow, Normal, Fast, Hyper) (Default: normal)...\n"
    )
    lines = 3
    while selection not in ("slow", "normal", "fast", "hyper", ""):
        lines += 3
        selection = input(
            "Game speed? \n(Slow, Normal, Fast, Hyper) (Default: normal)...\n"
        )
    speed_selection = selection if selection else "normal"
    speed_value = speed_defaults[speed_selection][0]
    pause_value = speed_defaults[speed_selection][1]
    print(("\033[F\033[K") * lines, end="\r")
    print(f"Speed: [{speed_selection}]")

    return Gamemode(
        players=player_selection,
        cpus=cpu_selection,
        speed=speed_value,
        pause=pause_value,
    )


def main():
    gamemode = create_gamemode()
    while True:
        gamemode.run_round()
        gamemode.eval_top_score()
        if gamemode.winner[1] != 0:
            break
    win_name, win_score = gamemode.winner
    print()
    print("******************************")
    print("******************************")
    print(f"  {win_name} WON")
    print(f"  {win_score} WON")
    print("******************************")
    print("******************************")
    _ = input()
    sys.exit()


if __name__ == "__main__":
    main()
