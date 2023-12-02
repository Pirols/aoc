from collections import defaultdict
from math import prod
from pathlib import Path


def solvea(configuration, data):
    valid_games_sum = 0
    for line in data.replace(";", ",").splitlines():
        game, combos = line.rstrip().split(":")
        for combo in combos.split(","):
            num, color = combo.split()
            if int(num) > configuration[color]:
                break
        else:
            valid_games_sum += int(game.replace("Game ", ""))

    return valid_games_sum


def solveb(data):
    total_power_set = 0
    for line in data.replace(";", ",").splitlines():
        _, combos = line.rstrip().split(":")
        min_combo = defaultdict(int)
        for combo in combos.split(","):
            num, color = combo.split()
            min_combo[color] = max(int(num), min_combo[color])
        total_power_set += prod(min_combo.values())

    return total_power_set


if __name__ == "__main__":
    ex_data = Path("example_data.txt").read_text()
    data = Path("data.txt").read_text()

    config_a = {"red": 12, "green": 13, "blue": 14}
    print(f"Part a (example): {solvea(config_a, ex_data)}")
    print(f"Part a: {solvea(config_a, data)}")

    print(f"Part b (example): {solveb(ex_data)}")
    print(f"Part b: {solveb(data)}")
