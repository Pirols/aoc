import copy

from pathlib import Path
from collections import defaultdict


def solve12a(connections, current_node, visited_small_caves):

    if current_node == 'end':
        return 1
    if current_node.islower():
        visited_small_caves.add(current_node)

    n_paths = 0
    for next_node in connections[current_node]:
        if next_node in visited_small_caves:
            continue
        n_paths += solve12a(connections, next_node, copy.deepcopy(visited_small_caves))

    return n_paths


def solve12b(connections, current_node, visited_small_caves, visited_twice):

    if current_node == 'end':
        return 1
    if current_node.islower():
        visited_small_caves.add(current_node)

    n_paths = 0
    for next_node in connections[current_node]:
        if next_node in visited_small_caves and (visited_twice or next_node == 'start'):
            continue
        if next_node in visited_small_caves and not visited_twice:
            n_paths += solve12b(connections, next_node, copy.deepcopy(visited_small_caves), True)
        else:
            n_paths += solve12b(connections, next_node, copy.deepcopy(visited_small_caves), visited_twice)

    return n_paths


if __name__ == "__main__":
    data_path = Path('12_data.txt')
    connections = defaultdict(list)

    with open(data_path, mode='r') as f:
        for line in f:
            a,b = line.rstrip().split('-')
            connections[a].append(b)
            connections[b].append(a)

    print(f"Number of connections entering small caves only once: {solve12a(connections, 'start', set())}")
    print(f"Number of connections entering small caves only once (except for one which can be visited twice): {solve12b(connections, 'start', set(), False)}")
