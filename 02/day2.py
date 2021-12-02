from pathlib import Path


def solve2a(path):
    hor, depth = 0, 0
    with open(path, mode='r') as f:
        for line in f:
            dir, val = line.split(' ')
            if dir == 'forward':
                hor += int(val)
            elif dir == 'down':
                depth += int(val)
            elif dir == 'up':
                depth -= int(val)
            else:
                print("unexpected direction")

    return hor*depth


def solve2b(path):
    hor, depth, aim = 0, 0, 0
    with open(path, mode='r') as f:
        for line in f:
            dir, val = line.split(' ')
            if dir == 'forward':
                num = int(val)
                hor += num
                depth += num*aim
            elif dir == 'down':
                aim += int(val)
            elif dir == 'up':
                aim -= int(val)
            else:
                print("unexpected direction")

    return hor*depth


if __name__ == "__main__":
    print(f"Product of horizontal and depth position: {solve2a(Path('02_data.txt'))}")
    print(f"Product of horizontal and depth position: {solve2b(Path('02_data.txt'))}")
