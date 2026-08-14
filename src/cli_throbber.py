import math
import multiprocessing
import time


class CLI_Throbber:
    def __init__(
        self,
        message: str = "",
        erase: bool = False,
        time: float = 0.0,
    ):

        self.message = message
        self.erase = erase
        self.time = time
        self.speed = 0.125
        self.adj_time = round(round(self.time / self.speed) * self.speed, 3)

        self.process = multiprocessing.Process(
            target=self.throb, args=(), name="CLI Throbber"
        )

    def throb(self):
        throbber = [
            "    \\. \\ ",
            ".   |'.| ",
            ".  /.'/  ",
            ".. | .|  ",
            "..  \\. \\ ",
            "... |'.| ",
            ".../.'/  ",
            "   | .|  ",
        ]
        n = 0
        t = 0
        size = 14
        bar = "|" + ("-" * size) + "|"
        copy = bar
        while True:
            if self.time > 0:
                print(f"\r{self.message} {bar} ", end="")
                t += self.speed
                bar = copy.replace("-", "#", math.ceil(size * (t / self.adj_time)))
            else:
                print(f"\r{self.message} {throbber[n]}", end="")

            n += 1
            if n >= len(throbber):
                n = 0

            time.sleep(self.speed)

    def start(self):
        self.process.start()
        if self.time > 0:
            if self.time >= self.speed:
                time.sleep(self.adj_time + 0.1)
                self.stop()
            else:
                print(self.message, end="")
                self.stop()

    def stop(self):
        if not self.process.is_alive():
            print("WARNGIN: CLI THROBBER NOT RUNNING")
        else:
            if self.erase:
                print("\033[F\033[K", end="\r")
            else:
                print()
            self.process.terminate()
