import statistics, math

from pathlib import Path


def solve7a(positions):

    median = int(statistics.median(positions))
    return sum(filter(lambda x: x > median, positions)) - sum(filter(lambda x: x < median, positions))

def solve7b(positions):

    mean = statistics.mean(positions)
    upper = math.ceil(mean)
    lower = math.floor(mean)
    res_upper = 0
    res_lower = 0

    for num in positions:
        res_upper += sum(range(1, abs(upper-num)+1))
        res_lower += sum(range(1, abs(lower-num)+1))

    return min(res_lower, res_upper)

if __name__ == "__main__":
    data_path = Path('07_data.txt')
    with open(data_path, mode='r') as fd:
        positions = [int(val) for val in fd.readline().rstrip().split(',')]

    print(f"Fuel spent to align crabs: {solve7a(positions)}")
    print(f"Fuel spent to align crabs (incremental cost version): {solve7b(positions)}")
