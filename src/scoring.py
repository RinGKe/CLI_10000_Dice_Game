from collections import Counter
from enum import Enum


class Combo(Enum):
    SPIDER_EYES = 10000
    DOUBLE_TRIPS = 2500
    FULLEST_HOUSE = 2000
    LARGE_STRAIGHT = 1500
    SMALL_STRAIGHT = 1000
    THREE_PAIRS = 750
    FULL_HOUSE = 600
    TWO_PAIRS = 250
    SIX_KIND = 400
    FIVE_KIND = 300
    FOUR_KIND = 200
    THREE_KIND = 100
    NONE = 1


def eval_dice(dice: list[int]) -> tuple[Combo, int, list[int]]:
    counts = Counter(dice)
    dice_set = set(dice)
    count_values = sorted(counts.values(), reverse=True)

    if dice == [1, 1, 1, 1, 1, 1]:
        return Combo.SPIDER_EYES, 0, []
    if sorted(dice) == [1, 2, 3, 4, 5, 6]:
        return Combo.LARGE_STRAIGHT, 0, []

    if {1, 2, 3, 4, 5}.issubset(dice_set) or {2, 3, 4, 5, 6}.issubset(dice_set):
        straight = (
            [1, 2, 3, 4, 5] if {1, 2, 3, 4, 5}.issubset(dice_set) else [2, 3, 4, 5, 6]
        )
        remaining = dice.copy()
        for d in straight:
            remaining.remove(d)
        return Combo.SMALL_STRAIGHT, 0, remaining

    if count_values == [3, 3]:
        return Combo.DOUBLE_TRIPS, 0, []
    if count_values == [2, 2, 2]:
        return Combo.THREE_PAIRS, 0, []
    if count_values == [4, 2]:
        return Combo.FULLEST_HOUSE, 0, []

    if count_values == [3, 2] or count_values == [3, 2, 1]:
        remaining = [d for d, c in counts.items() if c == 1]
        return Combo.FULL_HOUSE, 0, remaining

    if (
        count_values == [2, 2, 1, 1]
        or count_values == [2, 2, 1]
        or count_values == [2, 2]
    ):
        return Combo.TWO_PAIRS, 0, []

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


def score_dice(
    dice: list[int], addons: set[int]
) -> tuple[int, list[int], int, dict[str, int]]:
    combo, value, remaining = eval_dice(dice)
    new_addon = value
    value = 10 if value == 1 else value
    data: dict[str, int] = {}
    score = 0
    match combo:
        case Combo.SPIDER_EYES:
            score += Combo.SPIDER_EYES.value
            data["SPIDER EYES!"] = Combo.SPIDER_EYES.value

        case Combo.DOUBLE_TRIPS:
            score += Combo.DOUBLE_TRIPS.value
            data["Double Trips"] = Combo.DOUBLE_TRIPS.value

        case Combo.FULLEST_HOUSE:
            score += Combo.FULLEST_HOUSE.value
            data["Fullest House"] = Combo.FULLEST_HOUSE.value

        case Combo.LARGE_STRAIGHT:
            score += Combo.LARGE_STRAIGHT.value
            data["Large Straight"] = Combo.LARGE_STRAIGHT.value

        case Combo.SMALL_STRAIGHT:
            score += Combo.SMALL_STRAIGHT.value
            data["Small Straight"] = Combo.SMALL_STRAIGHT.value

        case Combo.THREE_PAIRS:
            score += Combo.THREE_PAIRS.value
            data["Three Pairs"] = Combo.THREE_PAIRS.value

        case Combo.FULL_HOUSE:
            score += Combo.FULL_HOUSE.value
            data["Full House"] = Combo.FULL_HOUSE.value

        case Combo.TWO_PAIRS:
            score += Combo.TWO_PAIRS.value
            data["Two Pairs"] = Combo.TWO_PAIRS.value

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

    for v in addons:
        if remaining.count(v) > 0:
            score += remaining.count(v) * 100
            data[f"Addons ({remaining.count(v)})"] = remaining.count(v) * 100
            remaining = [d for d in remaining if d != v]

    if remaining.count(1) > 0:
        score += remaining.count(1) * 100
        data[f"Ones ({remaining.count(1)})"] = remaining.count(1) * 100
        remaining = [d for d in remaining if d != 1]

    if remaining.count(5) > 0:
        score += remaining.count(5) * 50
        data[f"Fives ({remaining.count(5)})"] = remaining.count(5) * 50
        remaining = [d for d in remaining if d != 5]

    return score, remaining, new_addon, data
