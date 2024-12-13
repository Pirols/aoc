import graphlib
from collections import defaultdict


def main(fname):
    tot_correctly_ordered_median_num = 0
    tot_incorrectly_ordered_median_num = 0
    page_to_preceding_pages = defaultdict(list)
    with open(fname) as f:
        for line in f:
            if "|" in line:
                nums = line.split("|")
                page_to_preceding_pages[int(nums[0])].append(int(nums[1]))
            elif "," in line:
                nums = list(map(int, line.split(",")))
                ts = graphlib.TopologicalSorter()
                for num in nums:
                    for n in page_to_preceding_pages[num]:
                        if n in nums:
                            ts.add(n, num)
                correct_order = list(ts.static_order())
                if correct_order == nums:
                    tot_correctly_ordered_median_num += int(nums[len(nums)//2])
                else:
                    tot_incorrectly_ordered_median_num += int(correct_order[len(correct_order)//2])

    print(fname, "- solution 1:", tot_correctly_ordered_median_num)
    print(fname, "- solution 2:", tot_incorrectly_ordered_median_num)


if __name__ == "__main__":
    main("example_data.txt")
    main("data.txt")
