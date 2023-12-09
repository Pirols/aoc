from functools import reduce
from pathlib import Path


def solve(histories, first=False):
    tot = 0

    elems = []
    fn = (
        (lambda x, y: y-x) if first
        else (lambda x, y: y+x)
    )
    for hist in histories:
        red_hist = hist.copy()
        while any(el != 0 for el in red_hist):
            elems.append(red_hist[0 if first else -1])
            red_hist = [red_hist[i+1] - red_hist[i] for i in range(len(red_hist)-1)]
        tot += reduce(fn, [0] + elems[::-1])
        elems.clear()
    return tot


def get_histories(path):
    return [[int(x) for x in line.split(" ")] for line in path.read_text().splitlines()]


if __name__ == "__main__":
    ex_histories = get_histories(Path("example_data.txt"))
    histories = get_histories(Path("data.txt"))

    print(f"Part a (example): {solve(ex_histories)}")
    print(f"Part a: {solve(histories)}")

    print(f"Part b (example): {solve(ex_histories, first=True)}")
    print(f"Part b: {solve(histories, first=True)}")
