import re
from math import ceil, floor, prod, sqrt
from pathlib import Path


def beat_record(time, dist_to_beat):
    root = sqrt(time**2 - 4 * dist_to_beat)
    min_holding_time = ceil((time - root) / 2 + 1e-10)
    max_holding_time = floor((time + root) / 2 - 1e-10)
    return min_holding_time, max_holding_time


def n_ways_to_beat_record(time, dist_to_beat):
    a, b = beat_record(time, dist_to_beat)
    return b - a + 1


def solvea(races):
    return prod(n_ways_to_beat_record(time, best_dist) for time, best_dist in races)


def solveb(time, dist_to_beat):
    return n_ways_to_beat_record(time, dist_to_beat)


def get_races(txt):
    lines = txt.splitlines()
    num_regex = re.compile(r"(\d+)")

    times = num_regex.finditer(lines[0].split(":")[1])
    dists = num_regex.finditer(lines[1].split(":")[1])

    return tuple((int(time[0]), int(dist[0])) for time, dist in zip(times, dists))


if __name__ == "__main__":
    ex_races_a = get_races(Path("example_data.txt").read_text())
    races_a = get_races(Path("data.txt").read_text())

    print(f"Part a (example): {solvea(ex_races_a)}")
    print(f"Part a: {solvea(races_a)}")

    ex_race_b = tuple(
        int(line.split(":")[1])
        for line in Path("example_data.txt").read_text().replace(" ", "").split("\n")
    )
    race_b = tuple(
        int(line.split(":")[1])
        for line in Path("data.txt").read_text().replace(" ", "").split("\n")
    )

    print(f"Part b (example): {solveb(*ex_race_b)}")
    print(f"Part b: {solveb(*race_b)}")
