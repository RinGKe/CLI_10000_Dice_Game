from cli_throbber import CLI_Throbber


class Combo(Enum):
    DOUBLE_TRIPS = 1
    LARGE_STRAIGHT = 2
    FOUR_KIND = 3
    THREE_PAIRS = 4
    THREE_KIND = 5
    ONE = 6
    ADD_ON = 7
    FIVE = 8

def score_combo(combo=Combo, value=0) -> int:
    switch(combo):
        case DOUBLE_TRIPS:
            return 2500
        case LARGE_STRAIGHT:
            return 1500
        case FOUR_KIND:
            return value * 200
        case THREE_PAIRS:
            return 500
        case THREE_KIND:
            return value * 100
        case ONE:
        case ADD_ON:
            return 100
        case FIVE:
            return 50

class Dice:
    def __init__(self, amount=6) -> None:
        self.amount = amount
        self.active_dice = 6
        self.num_rolls = 0
        self.cup_num = 0
        self.current_score = 0
