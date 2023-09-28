from bisect import bisect_left
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        for i in range(length):
            to_find = target - numbers[i]
            index = binary_search(numbers, to_find)
            if index >= 0 and index != i:
                if index > i:
                    return [i+1, index+1]
                else:
                    return [index+1, i+1]


def binary_search(a, x, lo=0, hi=None):
    if hi is None: hi = len(a)
    pos = bisect_left(a, x, lo, hi)                  # find insertion position
    return pos if pos != hi and a[pos] == x else -1  # don't walk off the end