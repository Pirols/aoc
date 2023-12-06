from pathlib import Path


def solvea(data):
    blocks = data.split("\n\n")
    src = {int(n) for n in blocks.pop(0).split(": ")[1].rstrip().split(" ")}

    for block in blocks:
        dest = {}

        for line in block.rstrip().split("\n")[1:]:
            dest_range_start, src_range_start, range_length = (int(n) for n in line.split(" "))

            for el in src.difference(set(dest.keys())):
                if src_range_start <= el < src_range_start+range_length:
                    dest[el] = dest_range_start + el - src_range_start

        for el in src:
            if el not in dest:
                dest[el] = el
        src = set(dest.values())

    return min(src)


def solveb(data):
    # not feasible like this
    blocks = data.split("\n\n")
    nums = [int(n) for n in blocks.pop(0).split(": ")[1].rstrip().split(" ")]
    src = set()
    for i in range(len(nums))[::2]:
        src = src.union(set(range(nums[i], nums[i] + nums[i+1])))

    for block in blocks:
        dest = {}

        for line in block.rstrip().split("\n")[1:]:
            dest_range_start, src_range_start, range_length = (int(n) for n in line.split(" "))

            for el in src.difference(set(dest.keys())):
                if src_range_start <= el < src_range_start+range_length:
                    dest[el] = dest_range_start + el - src_range_start

        for el in src:
            if el not in dest:
                dest[el] = el
        src = set(dest.values())

    return min(src)


if __name__ == "__main__":
    ex_data = Path("example_data.txt").read_text()
    data = Path("data.txt").read_text()

    print(f"Part a (example): {solvea(ex_data)}")
    print(f"Part a: {solvea(data)}")

    print(f"Part b (example): {solveb(ex_data)}")
    print(f"Part b: {solveb(data)}")
