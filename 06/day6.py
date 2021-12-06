from pathlib import Path


def solve6(input_sequence, days):

    fishes = [input_sequence.count(i) for i in range(9)]

    for _ in range(days):
        newborns = fishes[0]
        fishes[:-1] = fishes[1:]
        fishes[6] += newborns
        fishes[8] = newborns

    return sum(fishes)


if __name__ == "__main__":
    data_path = Path('06_data.txt')

    with open(data_path, mode='r') as fd:
        input_sequence = [int(val) for val in fd.read().rstrip().split(',')]

    print(f"Number of lanternfishes after 80 days: {solve6(input_sequence, 80)}")
    print(f"Number of lanternfishes after 256 days: {solve6(input_sequence, 256)}")
