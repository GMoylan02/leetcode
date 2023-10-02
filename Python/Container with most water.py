class Solution:
    def maxArea(self, height: List[int]) -> int:
        h = lambda h1, h2, d: h1 * d if h1 < h2 else h2 * d
        max = 0
        left, right = 0, len(height)-1
        while left < right:
            hleft = height[left]
            hright = height[right]
            current = h(hleft, hright, right - left)
            if current > max:
                max = current
            if hleft <= hright:
                left += 1
            else:
                right -= 1
        return max