import numpy as np
import copy

from pathlib import Path


def get_adjacent_idx(i, j, w, h):

    if i < 0 or j < 0 or i >= w or j >= h:
        raise ValueError('Indices outside of shape')

    return [(i+r, j+c) for r in [-1,0,1] for c in [-1,0,1] \
            if (r != 0 or c != 0) and (0 <= i+r <= w-1) and (0 <= j+c <= h-1)]


def solve11a(octopus_energy_grid, n_steps):

    total_shines = 0
    grid_shape = octopus_energy_grid.shape

    for _ in range(n_steps):
        # reset shine matrix
        shine_matrix = np.zeros(grid_shape)

        # increase energy of the grid
        octopus_energy_grid += 1

        # shine
        shine_matrix[octopus_energy_grid > 9] = 1

        # propagate shines
        indices = np.where(shine_matrix)
        indices = list(zip(indices[0], indices[1]))
        while indices:
            idx = indices.pop()
            i, j = idx[0], idx[1]

            for adj_i, adj_j in get_adjacent_idx(i, j, grid_shape[0], grid_shape[1]):
                octopus_energy_grid[adj_i][adj_j] += 1

                if octopus_energy_grid[adj_i][adj_j] > 9 and not shine_matrix[adj_i][adj_j]:
                    shine_matrix[adj_i][adj_j] = 1
                    indices.append((adj_i, adj_j))

        # set to 0 octopuses which shined
        octopus_energy_grid[shine_matrix == 1] = 0

        # add shines to the total
        total_shines += np.sum(shine_matrix)

    return int(total_shines)


def solve11b(octopus_energy_grid):

    current_iteration = 1
    grid_shape = octopus_energy_grid.shape

    while True:
        # reset shine matrix
        shine_matrix = np.zeros(grid_shape)

        # increase energy of the grid
        octopus_energy_grid += 1

        # shine
        shine_matrix[octopus_energy_grid > 9] = 1

        # propagate shines
        indices = np.where(shine_matrix)
        indices = list(zip(indices[0], indices[1]))
        while indices:
            idx = indices.pop()
            i, j = idx[0], idx[1]

            for adj_i, adj_j in get_adjacent_idx(i, j, grid_shape[0], grid_shape[1]):
                octopus_energy_grid[adj_i][adj_j] += 1

                if octopus_energy_grid[adj_i][adj_j] > 9 and not shine_matrix[adj_i][adj_j]:
                    shine_matrix[adj_i][adj_j] = 1
                    indices.append((adj_i, adj_j))

        # set to 0 octopuses which shined
        octopus_energy_grid[shine_matrix == 1] = 0

        # iterate until during one iteration all octopuses flash together
        if shine_matrix.all():
            break

        current_iteration += 1

    return current_iteration


if __name__ == "__main__":
    data_path = Path('11_data.txt')

    with open(data_path, mode='r') as f:
        octopus_energy_grid = np.array([[int(val) for val in line.rstrip()] for line in f.readlines()])

    print(f"Number of flashes by 100th iteration: {solve11a(copy.deepcopy(octopus_energy_grid), 100)}")
    print(f"Index of first iteration during which all octopuses shined: {solve11b(octopus_energy_grid)}")
