from itertools import cycle
from math import lcm
from pathlib import Path


def solve(plan, map, starting_nodes):
    current_nodes = starting_nodes.copy()
    n_steps_node = {node: 0 for node in starting_nodes}

    for i, node in enumerate(current_nodes):
        for direction in cycle(plan):
            if current_nodes[i].endswith("Z"):
                break

            current_nodes[i] = map[current_nodes[i]][direction]
            n_steps_node[node] += 1

    return lcm(*n_steps_node.values())


def _get_map(lines):
    map = {}
    for line in lines:
        pos, lr = line.split(" = ")
        left, right = lr.lstrip("(").rstrip(")").split(", ")
        map[pos] = {"L": left, "R": right}
    return map


def get_data(lines):
    return lines[0], _get_map(lines[2:])


if __name__ == "__main__":
    ex_plan_a, ex_map_a = get_data(Path("example_data_a.txt").read_text().splitlines())
    ex_plan_b, ex_map_b = get_data(Path("example_data_b.txt").read_text().splitlines())
    plan, map = get_data(Path("data.txt").read_text().splitlines())

    print(f"Part a (example): {solve(ex_plan_a, ex_map_a, ['AAA'])}")
    print(f"Part a: {solve(plan, map, ['AAA'])}")

    print(f"Part b (example): {solve(ex_plan_b, ex_map_b, [x for x in ex_map_b.keys() if x.endswith('A')])}")
    print(f"Part b: {solve(plan, map, [x for x in map.keys() if x.endswith('A')])}")
