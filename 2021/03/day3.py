from pathlib import Path


def solve3a(path):
    with open(path, mode='r') as f:
        line = f.readline().rstrip()
        counts = [0]*len(line)
        while line:
            for i, num in enumerate(line):
                if num == '1':
                    counts[i] += 1
                elif num == '0':
                    counts[i] -= 1
                else:
                    print(f'char \'{num}\' was found.')
            line = f.readline().rstrip()

    gamma = 0
    epsilon = 0
    bin_len = len(counts)
    for i in range(bin_len):
        if counts[i] > 0:
            gamma += 2**(bin_len - i - 1)
        elif counts[i] < 0:
            epsilon += 2**(bin_len - i - 1)
        else:
            print(f'0 and 1 bits are equally likely for index {i}')

    return gamma*epsilon


def solve3b(path):

    with open(path, mode='r') as f:
        binaries = f.readlines()

    if binaries:
        bin_len = len(binaries[0].rstrip())
    else:
        return 0

    prefix_mst = ''
    prefix_lst = ''

    found_mst = False
    found_lst = False

    for bit_idx in range(bin_len):
        counter_mst = 0
        counter_lst = 0
        left_mst = 0
        left_lst = 0

        for binary in binaries:
            if not found_mst and binary.startswith(prefix_mst):
                counter_mst += 1 if binary[bit_idx] == '1' else -1
                left_mst += 1
            if not found_lst and binary.startswith(prefix_lst):
                counter_lst += 1 if binary[bit_idx] == '1' else -1
                left_lst += 1

        if left_mst == 1:
            found_mst = True
        if left_lst == 1:
            found_lst = True

        if not found_mst:
            if counter_mst >= 0:
                prefix_mst += '1'
            else:
                prefix_mst += '0'

        if not found_lst:
            if counter_lst >= 0:
                prefix_lst += '0'
            else:
                prefix_lst += '1'

    if found_mst:
        for binary in binaries:
            if binary.startswith(prefix_mst):
                prefix_mst = binary

    if found_lst:
        for binary in binaries:
            if binary.startswith(prefix_lst):
                prefix_lst = binary

    return int(prefix_mst, 2)*int(prefix_lst, 2)


if __name__ == "__main__":
    print(f"Power consumption of submarine: {solve3a(Path('03_data.txt'))}")
    print(f"Life supporting rate: {solve3b(Path('03_data.txt'))}")
