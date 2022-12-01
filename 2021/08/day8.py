from pathlib import Path
from collections import defaultdict


def solve8a(output_values):

    count = 0
    unique_sizes = {2, 3, 4, 7}

    for out_nums in output_values:
        count += sum([1 for out_num in out_nums if len(out_num) in unique_sizes])

    return count


def solve8b(unique_signal_patterns, output_values):

    # accumulation variable
    summed_outputs = 0

    # seven-digit display
    correct_mapping = {
        'abcefg':  '0',
        'cf':      '1',
        'acdeg':   '2',
        'acdfg':   '3',
        'bcdf':    '4',
        'abdfg':   '5',
        'abdefg':  '6',
        'acf':     '7',
        'abcdefg': '8',
        'abcdfg':  '9'
    }

    for i, usp in enumerate(unique_signal_patterns):
        # sort signals by len to be able to retrieve one, four, seven and eight easily
        usp = sorted(usp, key=len)

        one, seven, four, eight = usp[0], usp[1], usp[2], usp[-1]

        error_mapping = dict()

        # one is {c, f}, while seven is {a, c, f}, therefore the missing value from one maps to a
        error_mapping['a'] = (set(seven) - set(one)).pop()

        # count the occurrences of each letter (b, c, e and f all have a unique frequency)
        count_occurrences = defaultdict(int)
        for signal in usp:
            for letter in signal:
                count_occurrences[letter] += 1

        # letter a is already mapped and has the same number of occurrences of letter c, better disregard it
        count_occurrences[error_mapping['a']] = 0

        # get b,c,e and f mappings
        count_occurrences_reverted = {v:k for k,v in count_occurrences.items() if v != 7}
        error_mapping['b'] = count_occurrences_reverted[6]
        error_mapping['c'] = count_occurrences_reverted[8]
        error_mapping['e'] = count_occurrences_reverted[4]
        error_mapping['f'] = count_occurrences_reverted[9]

        # the only letter missing among the four's encoding is that mapping to d
        error_mapping['d'] = (set(four) - set(error_mapping.values())).pop()

        # the only letter missing is that mapping to g (which is also the last missing letter)
        error_mapping['g'] = (set(eight) - set(error_mapping.values())).pop()

        # get relevant output value
        output_sequence = output_values[i]
        output_string = ''

        # used to decode the output sequences
        error_mapping_reverted = {v:k for k,v in error_mapping.items()}

        for elem in output_sequence:
            output_string += correct_mapping["".join(sorted([error_mapping_reverted[letter] for letter in elem]))]

        summed_outputs += int(output_string)

    return summed_outputs


if __name__ == "__main__":
    data_path = Path('08_data.txt')

    unique_signal_patterns = list()
    output_values = list()

    with open(data_path, mode='r') as f:
        for line in f:
            samples, four_digits = line.split('|')
            unique_signal_patterns.append(samples.strip().split(' '))
            output_values.append(four_digits.strip().split(' '))

    print(f"Number of occurrences of 1,4,7 or 8: {solve8a(output_values)}")
    print(f"Sum of all output values: {solve8b(unique_signal_patterns, output_values)}")
