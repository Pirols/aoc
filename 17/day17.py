"""This script is a mess, I couldn't figure where the errors were and why it works!"""
from math import sqrt
from pathlib import Path


def overshoots_vertical(vy, y_min, y_max):
    y = 0
    max_height = 0

    while y > y_max:
        y += vy
        vy -= 1

        if max_height < y:
            max_height = y

    return not (y_min <= y <= y_max), max_height


def overshoots_horizontal(vx, x_min, x_max):
    x = 0

    while vx != 0 and x < x_min:
        x += vx
        vx -= 1

    return not (x_min <= x <= x_max)


def overshooots(vx, vy, x_min, x_max, y_min, y_max):
    x, y = 0, 0

    while True:
        if vx:
            vx -= 1
        vy -= 1

        x += vx
        y += vy

        if y_min <= y <= y_max and x_min <= x <= x_max:
            return False
        if x > x_max:
            return True
        if y < y_min:
            return True


if __name__ == "__main__":
    data_path = Path('17_data.txt')

    with open(data_path, mode='r') as f:
        target_data = f.readline().rstrip()

        x_min = int(target_data[target_data.index('x')+2:target_data.index('.')])
        x_max = int(target_data[target_data.index('.')+2:target_data.index(',')])

        y_min = int(target_data[target_data.index('y')+2:target_data.rindex('.')-1])
        y_max = int(target_data[target_data.rindex('.')+1:])

    possible_vx = set()
    possible_vy = set()
    max_height = 0

    for vx_proposal in range(round(sqrt(x_min*2)), x_max+1):
        if not overshoots_horizontal(vx_proposal, x_min, x_max):
            possible_vx.add(vx_proposal)

    y_bound = max(abs(y_min), abs(y_max))
    for vy_proposal in range(-y_bound, y_bound+1):
        over, height = overshoots_vertical(vy_proposal, y_min, y_max)
        if not over:
            possible_vy.add(vy_proposal)
            if max_height < height:
                max_height = height

    # could be optimized massively (e.g. noting the steps each possible velocity is within the target and matching them)
    count = 0
    for vx_proposal in range(round(sqrt(x_min*2))+1, x_max+2):
        for vy_proposal in range(-y_bound, y_bound+1):
            count += not overshooots(vx_proposal, vy_proposal, x_min, x_max, y_min, y_max)
            if vx_proposal > x_max:
                print(overshooots(vx_proposal, vy_proposal, x_min, x_max, y_min, y_max))

    print(f"Maximum height that can be reached: {max_height}")
    print(f"Number of distinct possible initial velocities: {count}")
