import heapq

from pathlib import Path


class Node:
    def __init__(self, x, y, risk_level):
        # coordinates
        self.x = x
        self.y = y

        # risk level
        self.risk_level = risk_level

        # A_star values
        self.neighbors = []
        self.f = 0
        self.g = float('inf')
        self.h = 0


    def set_neighbor(self, neighbor):
        self.neighbors.append(neighbor)


    def set_f(self, f):
        self.f = f


    def __lt__(self, other):
        return self.f < other.f


    def __repr__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)


def A_star(start, goal):
    # instantiate data structures
    opened = list()
    heapq.heapify(opened)
    closed = set()

    # initialize neighbors of starting node
    for neighbor in start.neighbors:
        neighbor.g = neighbor.risk_level
        neighbor.f = neighbor.h + neighbor.g
        heapq.heappush(opened, (neighbor.f, neighbor))

    # iterate until you reach the goal
    while opened:
        # extract best node based on f
        _, next_node = heapq.heappop(opened)
        closed.add(next_node)

        if next_node == goal:
            return next_node.f

        for neighbor in next_node.neighbors:
            if neighbor not in closed:
                neighbor.g = min(neighbor.g, next_node.g + neighbor.risk_level)
                neighbor.f = neighbor.h + neighbor.g
                if (neighbor.f, neighbor) not in opened:
                    heapq.heappush(opened, (neighbor.f, neighbor))

    return -1


def elevate_risk(risk_level, step):
    elevated_risk_level = (risk_level + step) % 10
    if elevated_risk_level < risk_level:
        elevated_risk_level += 1
    return elevated_risk_level


if __name__ == "__main__":
    data_path = Path('15_data.txt')

    # part a grid
    grid_a = dict()
    n_lines_a = 0
    width_a = 0
    # part b grid
    grid_b = dict()
    n_lines_b = 0
    width_b = 0

    with open(data_path, mode='r') as f:
        # create nodes
        for i, line in enumerate(f):
            n_lines_a += 1
            width_a = len(line) - 1
            for j, risk in enumerate(line.rstrip()):
                grid_a[(i, j)] = Node(i, j, int(risk))
                grid_b[(i, j)] = Node(i, j, int(risk))

    # assign neighbors and set h for each node in grid_a
    for i in range(n_lines_a):
        for j in range(width_a):
            node = grid_a[(i, j)]
            node.h = manhattan_distance(node.x, node.y, n_lines_a-1, width_a-1)
            if i > 0:
                node.set_neighbor(grid_a[(i-1, j)])
            if j > 0:
                node.set_neighbor(grid_a[(i, j-1)])
            if i < n_lines_a - 1:
                node.set_neighbor(grid_a[(i+1, j)])
            if j < width_a - 1:
                node.set_neighbor(grid_a[(i, j+1)])

    # set starting node's g to 0
    grid_a[(0, 0)].g = 0

    # set part b grid's dimensions
    n_lines_b = n_lines_a*5
    width_b = width_a*5

    # increase grid_b by 5 times vertically (stack grid_a horizontally elevating risk)
    for i in range(n_lines_a):
        for j in range(width_a):
            for k in range(1, 5):
                grid_b[(i, j+k*width_a)] = Node(i, j+k*width_a, elevate_risk(grid_b[(i, j)].risk_level, k))

    # increase grid_b by 5 times horizontally (stack grid_a vertically elevating risk)
    for j in range(width_b):
        for i in range(n_lines_a):
            for k in range(1, 5):
                grid_b[(i+k*n_lines_a, j)] = Node(i+k*n_lines_a, j, elevate_risk(grid_b[(i, j)].risk_level, k))

    # assign neighbors and set h for each node in grid_b
    for i in range(n_lines_b):
        for j in range(width_b):
            node = grid_b[(i, j)]
            node.h = manhattan_distance(node.x, node.y, n_lines_b-1, width_b-1)
            if i > 0:
                node.set_neighbor(grid_b[(i-1, j)])
            if j > 0:
                node.set_neighbor(grid_b[(i, j-1)])
            if i < n_lines_b - 1:
                node.set_neighbor(grid_b[(i+1, j)])
            if j < width_b - 1:
                node.set_neighbor(grid_b[(i, j+1)])

    # part a
    print(f"Minimum risk of possible paths from start to finish: {A_star(grid_a[(0, 0)], grid_a[(n_lines_a-1, width_a-1)])}")

    # part b
    print(f"Minimum risk of possible paths from start to finish: {A_star(grid_b[(0, 0)], grid_b[(n_lines_b-1, width_b-1)])}")
