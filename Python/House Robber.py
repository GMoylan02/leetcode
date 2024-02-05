class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        result = max(nums[0], nums[1])
        if len(nums) == 2:
            return result

        for i in range(2, len(nums)):
            if i == 2:
                nums[i] += nums[i-2]
            elif i >= 3:
                nums[i] += max(nums[i-3], nums[i-2])
            if nums[i] > result:
                result = nums[i]
        return result