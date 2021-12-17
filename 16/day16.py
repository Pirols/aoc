from math import prod
from pathlib import Path


def hex2bin(hex_str):
    return "".join([bin(int(hex_char, 16))[2:].zfill(4) for hex_char in hex_str])


def bin2int(bin_str):
    return int(bin_str, 2)


def get_literal_value(bin_str):
    # initialize variables
    lit_bin_str = ""
    i = 0

    while True:
        # discard first bit
        i += 1
        lit_bin_str += bin_str[i :i+4]
        i += 4

        # if first bit was a 0 this is the last portion of the literal
        if bin_str[i-5] == '0':
            break

    lit_val = bin2int(lit_bin_str)
    return lit_val, i


def parse_packet(packet):
    # initialize index
    i = 0

    # version of packet
    ver_sum = bin2int(packet[i:i+3])
    i += 3

    # type of packet
    type_id = bin2int(packet[i:i+3])
    i += 3

    # literal packet
    if type_id == 4:
        lit_val, lit_len = get_literal_value(packet[i:])
        i += lit_len
        return ver_sum, i, lit_val

    # operator packet
    else:
        length_type_id = int(packet[i])
        i += 1

        # store results
        results = list()

        if length_type_id:
            # next 11 bits encode the number of sub-packets that follow
            i += 11
            for _ in range(bin2int(packet[i-11:i])):
                ver_add, i_add, res = parse_packet(packet[i:])
                ver_sum += ver_add
                i += i_add
                results.append(res)
        else:
            # next 15 bits encode total length in bits of sub-packets
            n_bits = bin2int(packet[i:i+15])
            i += 15
            while n_bits > 0:
                ver_add, i_add, res = parse_packet(packet[i:])
                ver_sum += ver_add
                i += i_add
                n_bits -= i_add
                results.append(res)

        return ver_sum, i, OPERATIONS[type_id](results)


if __name__ == "__main__":
    data_path = Path('16_data.txt')

    with open(data_path, mode='r') as f:
        hex_data = f.readline().rstrip()
    bin_data = hex2bin(hex_data)

    OPERATIONS = {
        0: sum,
        1: prod,
        2: min,
        3: max,
        5: lambda vals: vals[0] > vals[1],
        6: lambda vals: vals[0] < vals[1],
        7: lambda vals: vals[0] == vals[1]
    }
    ver_sum, i, res = parse_packet(bin_data)

    # part a
    print(f"Sum of packets' version numbers {ver_sum}")
    # part b
    print(f"Sum of packets' version numbers {res}")
