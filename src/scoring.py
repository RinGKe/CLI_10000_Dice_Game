from collections import Counter
from enum import Enum


class Combo(Enum):
    DOUBLE_TRIPS = 2500
    LARGE_STRAIGHT = 1500
    SIX_KIND = 800
    FIVE_KIND = 400
    FOUR_KIND = 200
    THREE_PAIRS = 500
    THREE_KIND = 100
    NONE = 1


def eval_dice(dice: list[int]) -> tuple[Combo, int, list[int]]:
    counts = Counter(dice)
    count_values = sorted(counts.values(), reverse=True)

    if sorted(dice) == [1, 2, 3, 4, 5, 6]:
        return Combo.LARGE_STRAIGHT, 0, []
    if count_values == [3, 3]:
        return Combo.DOUBLE_TRIPS, 0, []
    if count_values == [2, 2, 2]:
        return Combo.THREE_PAIRS, 0, []

    top_val, top_count = counts.most_common(1)[0]
    remaining = [d for d in dice if d != top_val]
    if top_count == 6:
        return Combo.SIX_KIND, top_val, []
    if top_count == 5:
        return Combo.FIVE_KIND, top_val, remaining
    if top_count == 4:
        return Combo.FOUR_KIND, top_val, remaining
    if top_count == 3:
        return Combo.THREE_KIND, top_val, remaining

    return Combo.NONE, 0, dice


def score_dice(dice: list[int]) -> tuple[int, list[int], dict[str, int]]:
    combo, value, remaining = eval_dice(dice)
    value = 10 if value == 1 else value
    data = {}
    score = 0
    match combo:
        case Combo.DOUBLE_TRIPS:
            score += Combo.DOUBLE_TRIPS.value
            data["Double Trips"] = Combo.DOUBLE_TRIPS.value

        case Combo.LARGE_STRAIGHT:
            score += Combo.LARGE_STRAIGHT.value
            data["Large Straight"] = Combo.LARGE_STRAIGHT.value

        case Combo.THREE_PAIRS:
            score += Combo.THREE_PAIRS.value
            data["Three Pairs"] = Combo.THREE_PAIRS.value

        case Combo.SIX_KIND:
            score += value * Combo.SIX_KIND.value
            data[f"Six of a kind ({value})"] = value * Combo.SIX_KIND.value

        case Combo.FIVE_KIND:
            score += value * Combo.FIVE_KIND.value
            data[f"Five of a kind ({value})"] = value * Combo.FIVE_KIND.value

        case Combo.FOUR_KIND:
            score += value * Combo.FOUR_KIND.value
            data[f"Four of a kind ({value})"] = value * Combo.FOUR_KIND.value

        case Combo.THREE_KIND:
            score += value * Combo.THREE_KIND.value
            data[f"Three of a kind ({value})"] = value * Combo.THREE_KIND.value

        case Combo.NONE:
            pass

    score += remaining.count(1) * 100
    if remaining.count(1) > 0:
        data["Ones"] = remaining.count(1) * 100

    score += remaining.count(5) * 50
    if remaining.count(5) > 0:
        data["Fives"] = remaining.count(5) * 50

    remaining = [d for d in remaining if (d != 1) and (d != 5)]

    return score, remaining, data
