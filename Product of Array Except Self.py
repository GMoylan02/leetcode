class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = nums[i-1] * prefix[i-1]
            postfix[len(nums) - 1 - i] = nums[len(nums) - i] * postfix[len(nums) - i]
        solution = [1] * len(nums)
        for i in range(len(nums)):
            solution[i] = prefix[i] * postfix[i]
        return solution