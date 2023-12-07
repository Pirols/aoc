from functools import lru_cache
from pathlib import Path

CARDS_RANKING = {
    **{
        str(i): i for i in range(1, 10)
    },  # "1": 1, "2": 2, "3": 3, …, "9": 9  -- 1 used as replacement for "J" under joker rules
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}


HANDS_RANKING = {
    "5k": 6,
    "4k": 5,
    "fh": 4,
    "3k": 3,
    "2p": 2,
    "2k": 1,
    "hc": 0,
}


def get_hand_type_rank(hand, joker=False):
    j_cond = joker and "J" in hand
    match len(unique_hand := set(hand)):
        case 1:
            return HANDS_RANKING["5k"]
        case 2:
            if j_cond:
                return HANDS_RANKING["5k"]
            if 2 in (hand.count(char) for char in unique_hand):
                return HANDS_RANKING["fh"]
            return HANDS_RANKING["4k"]
        case 3:
            if 2 in (hand.count(char) for char in unique_hand):
                if joker and (n_js := hand.count("J")):
                    if n_js == 1:
                        return HANDS_RANKING["fh"]
                    return HANDS_RANKING["4k"]
                return HANDS_RANKING["2p"]
            if j_cond:
                return HANDS_RANKING["4k"]
            return HANDS_RANKING["3k"]
        case 4:
            if j_cond:
                return HANDS_RANKING["3k"]
            return HANDS_RANKING["2k"]
        case 5:
            if j_cond:
                return HANDS_RANKING["2k"]
            return HANDS_RANKING["hc"]


@lru_cache
def better_hand(hand1, hand2, joker=False):
    """
    Return True if hand1 is stronger than hand2 and False otherwise
    """
    rank1 = get_hand_type_rank(hand1, joker=joker)
    rank2 = get_hand_type_rank(hand2, joker=joker)
    if rank1 != rank2:
        return rank1 > rank2

    for c1, c2 in zip(
        hand1.replace("J", "1") if joker else hand1,
        hand2.replace("J", "1") if joker else hand2,
    ):
        if c1 != c2:
            return CARDS_RANKING[c1] > CARDS_RANKING[c2]

    return False


def solve(data, joker=False):
    hands_sorted = []
    for line in data.splitlines():
        hand, bid = line.split(" ")

        for i, (old_hand, _) in enumerate(hands_sorted):
            if better_hand(old_hand, hand, joker=joker):
                hands_sorted.insert(i, (hand, int(bid)))
                break
        else:
            hands_sorted.append((hand, int(bid)))

    return sum((i + 1) * bid for i, (_, bid) in enumerate(hands_sorted))


if __name__ == "__main__":
    ex_data = Path("example_data.txt").read_text()
    data = Path("data.txt").read_text()

    print(f"Part a (example): {solve(ex_data)}")
    print(f"Part a: {solve(data)}")

    print(f"Part b (example): {solve(ex_data, joker=True)}")
    print(f"Part b: {solve(data, joker=True)}")
