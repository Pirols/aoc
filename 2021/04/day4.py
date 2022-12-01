import numpy as np

from pathlib import Path


def solve4a(num_sequence, tables):

    markers = np.array([np.zeros((5, 5)) for _ in tables])

    for num in num_sequence:
        for i, table in enumerate(tables):
            markers[i][table == num] = 1

            if any(np.sum(markers[i], axis=1) == 5) or any(np.sum(markers[i], axis=0) == 5):
                # found winning table
                return np.sum(table[markers[i] == 0] * num)

    return -1


def solve4b(num_sequence, tables):
    markers = np.array([np.zeros((5, 5)) for _ in tables])
    left_indices = set(range(len(tables)))

    for num in num_sequence:
        for i, table in enumerate(tables):
            if i not in left_indices:
                continue

            markers[i][table == num] = 1

            if any(np.sum(markers[i], axis=1) == 5) or any(np.sum(markers[i], axis=0) == 5):
                if len(left_indices) == 1:
                    # found last winning table
                    return np.sum(table[markers[i] == 0] * num)

                left_indices.remove(i)

    return -1


if __name__ == "__main__":
    data_path = Path('04_data.txt')
    tables = list()

    with open(data_path, mode='r') as fd:
        # get sequence of numbers
        num_sequence = [int(num) for num in fd.readline().rstrip().split(',')]

        fd.readline()       # discard first empty line
        new_table = list()  # initialize current table

        for line in fd:
            if line == "\n":
                # current table is full, add it to tables
                tables.append(new_table)
                new_table = list()
            else:
                # add current line to current table
                new_table.append([int(num) for num in line.rstrip().split()])
        # add last table
        tables.append(new_table)

    print(f"First winner final score: {solve4a(np.array(num_sequence), np.array(tables))}")
    print(f"Last winner final score: {solve4b(np.array(num_sequence), np.array(tables))}")
