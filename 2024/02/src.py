from pathlib import Path


def is_safe(nums, reduced_list=False):
    MIN_DIFF, MAX_DIFF = 1, 3
    inc = dec = False
    for idx in range(len(nums) - 1):
        diff = nums[idx+1] - nums[idx]
        if diff > 0:
            inc = True
        else:
            dec = True
        if (inc and dec) or not MIN_DIFF <= abs(diff) <= MAX_DIFF:
            return not reduced_list and (
                is_safe(nums[:idx-1] + nums[idx:], reduced_list=True)
                or
                is_safe(nums[:idx] + nums[idx+1:], reduced_list=True)
                or
                is_safe(nums[:idx+1] + nums[idx+2:], reduced_list=True)
            )
    return True



def solve(path, dampener=False):
    return sum(
        (
            is_safe(
                [int(n) for n in line.rstrip().split(" ")],
                reduced_list=not dampener,
            )
            for line in path.open()
        )
    )


if __name__ == "__main__":
    ex_path = Path("example_data.txt")
    path = Path("data.txt")

    print(f"Part a (example): {solve(ex_path)}")
    print(f"Part a: {solve(path)}")

    print(f"Part b (example): {solve(ex_path, dampener=True)}")
    print(f"Part b: {solve(path, dampener=True)}")
