class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        goal = sum(nums)
        if goal % 2 != 0:
            return False
        goal = goal // 2
        sub = {0, nums[0]}

        for num in nums[1:]:
            curr = sub.copy()
            for ele in curr:
                t = num + ele
                if t == goal:
                    return True
                sub.add(t)
        return False


