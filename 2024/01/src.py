from collections import defaultdict
from pathlib import Path


def solve_a(path):
    left = []
    right = []
    for line in path.open():
        left.append(int(line[:line.find(" ")]))
        right.append(int(line[line.rfind(" ") + 1:]))

    left.sort()
    right.sort()
    return sum(abs(left[i] - right[i]) for i in range(len(left)))


def solve_b(path):
    left = []
    right = defaultdict(int)
    for line in path.open():
        left.append(int(line[:line.find(" ")]))
        right[int(line[line.rfind(" ") + 1:])] += 1

    return sum(v * right[v] for v in left)


if __name__ == "__main__":
    ex_path = Path("example_data.txt")
    path = Path("data.txt")

    print(f"Part a (example): {solve_a(ex_path)}")
    print(f"Part a: {solve_a(path)}")

    print(f"Part b (example): {solve_b(ex_path)}")
    print(f"Part b: {solve_b(path)}")
