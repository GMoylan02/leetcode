class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        if res < nums[-1]:
            return res
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[r]:
                l = mid + 1
            elif nums[mid] <= nums[r]:
                r = mid - 1
        return res

