import math
import multiprocessing
import random
import threading
import time


class CLI_Throbber:
    def __init__(self, message="", time=3.0, speed=0.124) -> None:
        self.message = message
        self.time = time
        self.speed = speed

        self.process = multiprocessing.Process(
            target=self.throb, args=(), name="CLI Throbber"
        )

    def throb(self):
        throbber = [
            "(>'-')>   \\. \\ ",
            "(^'-')^   |'.| ",
            "^('-'^)  /.'/  ",
            "^('-'^)  | .|  ",
            "<('-'<)   \\. \\ ",
            "^('-'^)   |'.| ",
            "(^'-')^  /.'/  ",
            "(>'-')>  | .|  ",
        ]
        n = 0
        t = 0
        size = 35
        bar = "|" + ("-" * size) + "|"
        copy = bar
        while True:
            print(f"\r{self.message} {throbber[n]} {bar}", end="")
            n += 1
            t += self.speed
            bar = copy.replace("-", "#", math.ceil(size * (t / self.time)))
            if n >= len(throbber):
                n = 0
            time.sleep(self.speed)

    def start(self):
        self.process.start()
        time.sleep(self.time)
        self.stop()

    def stop(self):
        if not self.process.is_alive():
            print("WARNGIN: CLI THROBBER NOT RUNNING")
        else:
            self.process.terminate()
            print()


if __name__ == "__main__":
    throbber = CLI_Throbber("Rolling...", 2)
    throbber.start()
