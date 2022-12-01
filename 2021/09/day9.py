import math

from pathlib import Path


def solve9a(map):

    lows = set()

    n_lines = len(map)
    n_cols = len(map[0])

    for i, line in enumerate(map):
        for j, num in enumerate(line):
            if (i == 0 or map[i-1][j] > num) and \
               (j == 0 or map[i][j-1] > num) and \
               (i == n_lines - 1 or map[i+1][j] > num) and \
               (j == n_cols - 1 or map[i][j+1] > num):
                lows.add((i, j))

    return lows


def solve9b(map, i, j, visited):
    if (i, j) in visited or map[i][j] == 9:
        return 0
    visited.add((i, j))
    tot = 0
    if i != 0:
        tot += solve9b(map, i-1, j, visited)
    if i != len(map) - 1:
        tot += solve9b(map, i+1, j, visited)
    if j != 0:
        tot += solve9b(map, i, j-1, visited)
    if j != len(map) - 1:
        tot += solve9b(map, i, j+1, visited)
    return 1 + tot


if __name__ == "__main__":
    data_path = Path('09_data.txt')
    map = [[int(val) for val in line.rstrip()] for line in open(data_path, mode='r')]

    low_points = solve9a(map)

    print(f"Total risk level: {sum([1+map[i][j] for (i, j) in low_points])}")
    print(f"Three largest basins sizes: {math.prod(sorted([solve9b(map, i, j, set()) for (i, j) in low_points])[-3:])}")
