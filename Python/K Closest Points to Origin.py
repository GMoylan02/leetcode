class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = lambda p : p[0]**2 + p[1]**2
        return sorted(points, key=dist)[:k]