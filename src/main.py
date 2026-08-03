import readchar
from cli_throbber import CLI_Throbber

roll_throbber = CLI_Throbber("Press 'SPACE' to Roll...")


def main():
    roll_throbber.start()
    while True:
        key = readchar.readkey()
        if key == " ":
            roll_throbber.stop()
            print("rolled")
            break


if __name__ == "__main__":
    main()
