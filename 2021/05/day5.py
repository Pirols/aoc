import numpy as np

from pathlib import Path


def solve5a(data_path):

    # assuming maximum value is 999, kind of cheating
    map = np.zeros((999, 999))

    with open(data_path, mode='r') as fd:
        for line in fd:
            p1, _, p2 = line.split(" ")
            x1, y1 = [int(val) for val in p1.split(",")]
            x2, y2 = [int(val) for val in p2.split(",")]

            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    map[x1][y] += 1

            elif y1 == y2:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    map[x][y1] += 1

            else:
                continue

    return np.sum(map >= 2)


def solve5b(data_path):

    # assuming maximum value is 999, kind of cheating
    map = np.zeros((999, 999))

    with open(data_path, mode='r') as fd:
        for line in fd:
            p1, _, p2 = line.split(" ")
            x1, y1 = [int(val) for val in p1.split(",")]
            x2, y2 = [int(val) for val in p2.split(",")]

            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    map[x1][y] += 1

            elif y1 == y2:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    map[x][y1] += 1

            else:
                x_inc = 1 if x1 < x2 else -1
                y_inc = 1 if y1 < y2 else -1

                while x1 != x2+x_inc:
                    map[x1][y1] += 1
                    x1 += x_inc
                    y1 += y_inc

    return np.sum(map >= 2)


if __name__ == "__main__":
    data_path = Path('05_data.txt')

    print(f"Number of 2 or more intersections (without diagonal lines): {solve5a(data_path)}")
    print(f"Number of 2 or more intersections: {solve5b(data_path)}")
