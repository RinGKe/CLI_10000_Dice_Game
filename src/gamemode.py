import time

from .player import CPU, Player


class Gamemode:
    def __init__(
        self,
        players: int = 1,
        cpus: int = 1,
        score: int = 10000,
        threshold: int = 500,
        pause: float = 1.0,
        speed: float = 1.0,
    ):

        self.win_score = score
        self.speed = speed
        self.pause = pause
        self.round = 0
        self.winner = ("", 0)
        self.players = [
            Player(f"Player {x + 1}", threshold) for x in range(players)
        ] + [CPU(f"CPU {x + 1}", threshold) for x in range(cpus)]

    def run_round(self) -> None:
        self.round += 1
        print()
        print()
        print("                          \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
        print(f"                                    ROUND {self.round}")
        print("                          ////////////////////")
        for p in self.players:
            time.sleep(self.pause)

            print()
            print()
            print("                          //////////")
            print(f"                           {p.name}")
            print("                          \\\\\\\\\\\\\\\\\\\\")

            time.sleep(self.pause)

            p.play_turn(self.speed)

    def eval_top_score(self) -> None:
        time.sleep(self.pause)
        places = sorted(self.players, key=lambda x: x.score, reverse=True)
        print()
        print("        ============================")
        print(f"         [Round {self.round} results]")
        longest = 0
        for p in places:
            longest = max(len(p.name), longest)
        for i, p in enumerate(places):
            len_dif = longest - len(p.name)
            buffer = " " * (1 if ((i + 1) < 10) and len(places) > 9 else 0)
            print(f"           {i + 1}: {buffer}{p.name} {'-' * len_dif}--> {p.score}")
        print("        ============================")
        if places[0].score >= self.win_score:
            self.winner = (places[0].name, places[0].score)
        time.sleep(max(self.pause * 2, 2))
