# if mid in left sorted portion and target < mid, check target with nums[l] to see if target is left or right of mid
# if mid in right sorted portion and target > mid, check target with nums[r] to see if target is left or right of mid

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            # If in left sorted portion
            if nums[mid] >= nums[l]:
                if target < nums[mid] and target >= nums[l]:
                    r = mid-1
                else:
                    l = mid+1
            # If in right sorted portion
            else:
                if target > nums[mid] and target <= nums[r]:
                    l = mid+1
                else:
                    r = mid-1
        return -1