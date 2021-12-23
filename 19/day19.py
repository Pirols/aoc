import numpy as np
from pathlib import Path
from collections import defaultdict


ROT_MATRICES = [
    np.array([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
    ]),
    np.array([
        [1, 0, 0],
        [0, -1, 0],
        [0, 0, -1],
    ]),
    np.array([
        [1, 0, 0],
        [0, 0, 1],
        [0, -1, 0],
    ]),
    np.array([
        [1, 0, 0],
        [0, 0, -1],
        [0, 1, 0],
    ]),
    np.array([
        [-1, 0, 0],
        [0, 1, 0],
        [0, 0, -1],
    ]),
    np.array([
        [-1, 0, 0],
        [0, -1, 0],
        [0, 0, 1],
    ]),
    np.array([
        [-1, 0, 0],
        [0, 0, -1],
        [0, -1, 0],
    ]),
    np.array([
        [-1, 0, 0],
        [0, 0, 1],
        [0, 1, 0],
    ]),
    np.array([
        [0, -1, 0],
        [1, 0, 0],
        [0, 0, 1],
    ]),
    np.array([
        [0, 0, -1],
        [1, 0, 0],
        [0, -1, 0],
    ]),
    np.array([
        [0, 1, 0],
        [1, 0, 0],
        [0, 0, -1],
    ]),
    np.array([
        [0, 0, 1],
        [1, 0, 0],
        [0, 1, 0],
    ]),
    np.array([
        [0, -1, 0],
        [-1, 0, 0],
        [0, 0, -1],
    ]),
    np.array([
        [0, 0, -1],
        [-1, 0, 0],
        [0, 1, 0],
    ]),
    np.array([
        [0, 0, 1],
        [-1, 0, 0],
        [0, -1, 0],
    ]),
    np.array([
        [0, 1, 0],
        [-1, 0, 0],
        [0, 0, 1],
    ]),
    np.array([
        [0, 0, -1],
        [0, 1, 0],
        [1, 0, 0],
    ]),
    np.array([
        [0, -1, 0],
        [0, 0, -1],
        [1, 0, 0],
    ]),
    np.array([
        [0, 0, 1],
        [0, -1, 0],
        [1, 0, 0],
    ]),
    np.array([
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 0],
    ]),
    np.array([
        [0, -1, 0],
        [0, 0, 1],
        [-1, 0, 0],
    ]),
    np.array([
        [0, 0, 1],
        [0, 1, 0],
        [-1, 0, 0],
    ]),
    np.array([
        [0, 1, 0],
        [0, 0, -1],
        [-1, 0, 0],
    ]),
    np.array([
        [0, 0, -1],
        [0, -1, 0],
        [-1, 0, 0],
    ]),
]


class Scanner:

    def __init__(self, id, position=None):
        self.id = id
        self.position = position
        self.beacons = []


    def insert_beacon(self, beacon):
        self.beacons.append(beacon)


    def rototranslate(self, P, R):
        pos = np.array(P)
        for i in range(len(self.beacons)):
            self.beacons[i] = np.matmul(R, self.beacons[i]) + pos
            self.position = pos


def locate_scanner(located_scanner, unlocated_scanner):

    for R in ROT_MATRICES:
        distances = defaultdict(int)
        for beacon in located_scanner.beacons:
            for other in unlocated_scanner.beacons:
                other_rotated = np.matmul(R, other)
                distances[get_manhattan_distance(beacon, other_rotated)] += 1

        for dist, num in distances.items():
            if num >= 12:
                return dist, R

    return None, None


def get_manhattan_distance(point1, point2):
    return tuple(point1-point2)


if __name__ == "__main__":
    data_path = Path('19_data.txt')
    scanners = list()
    scanner_id = -1

    with open(data_path, mode='r') as f:
        for line in f:
            if line.startswith('---'):
                # new scanner
                scanner_id += 1
                scanners.append(Scanner(scanner_id))
            elif line != '\n':
                x,y,z = [int(val) for val in line.rstrip().split(',')]
                scanners[-1].insert_beacon(np.array([x, y, z]))

    # fix first scanner's position
    scanners[0].position = np.array([0, 0, 0])

    # split scanners among located ones and non located ones
    located = [scanners[0]]
    unlocated = scanners[:]

    # iterate until all scanners' positions have been determined
    while len(located) != len(unlocated):
        for known in located:
            for unknown in unlocated:
                if unknown in located:
                    continue
                P, R = locate_scanner(known, unknown)

                if P is not None:
                    unknown.rototranslate(P, R)
                    located.append(unknown)
                    break

    points = set()
    for scanner in located:
        for beacon in scanner.beacons:
            points.add(tuple(beacon))

    # part a
    print(f"Number of different beacons: {len(points)}")

    # part b
    max_dist_scan = 0
    for i in range(len(located)):
        for j in range(i+1, len(located)):
            cur_dist = np.sum(np.abs(get_manhattan_distance(located[i].position, located[j].position)))
            if cur_dist > max_dist_scan:
                max_dist_scan = cur_dist
    print(f"Maximum distance among scanners: {max_dist_scan}")
