class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            mid = (l + r) // 2
            time_taken = 0
            for p in piles:
                time_taken += math.ceil(float(p) / mid)
            if time_taken > h:
                l = mid + 1
            else:
                res = mid
                r = mid - 1
        return res