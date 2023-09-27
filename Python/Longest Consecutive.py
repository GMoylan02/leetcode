class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        nums.sort()
        longest = 0
        current = 1
        nums = remove_dupes_from_sorted(nums)
        if len(nums) == 1:
            return 1
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]+1:
                current +=1
            if current > longest:
                longest = current
            if nums[i+1] != nums[i]+1:
                current = 1
        return longest

def remove_dupes_from_sorted(nums):
    result = []
    for i in nums:
        if len(result) == 0 or not result[-1] == i:
            result.append(i)
    return result