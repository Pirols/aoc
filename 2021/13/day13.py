import numpy as np

from pathlib import Path


def fold(grid, dir, num):

    if dir == 'x':
        flipped_part = np.flip(grid[:, num+1:], axis=1)
        out_grid = np.logical_or(grid[:, num-flipped_part.shape[1]:num], flipped_part)

    else:
        flipped_part = np.flip(grid[num+1:, :], axis=0)
        out_grid = np.logical_or(grid[num-flipped_part.shape[0]:num, :], flipped_part)

    return out_grid


if __name__ == "__main__":
    data_path = Path('13_data.txt')

    with open(data_path, mode='r') as f:
        dots = list()
        max_x = 0
        max_y = 0
        for line in f:
            line = line.rstrip()
            if line == '':
                break
            x, y = [int(val) for val in line.split(',')]
            max_x, max_y = max(x, max_x), max(y, max_y)
            dots.append((x, y))
        folds = list()
        for line in f:
            fields = line.rstrip().split(' ')
            dir,val = fields[2].split('=')
            folds.append((dir, int(val)))

    grid = np.zeros((max_y+1, max_x+1), dtype=np.uint8)

    for dot in dots:
        grid[dot[1],dot[0]] = 1

    # part1
    first_fold = folds[0]
    after_first_fold_grid = fold(grid, first_fold[0], first_fold[1])

    final_grid = grid
    for dir, num in folds:
        final_grid = fold(final_grid, dir, num)

    print(f"Number of visible dots after first fold: {int(np.sum(after_first_fold_grid))}")
    print(np.array(final_grid, dtype=np.uint8))
