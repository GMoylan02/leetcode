class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        u, d = 0, len(matrix) - 1
        while u <= d:
            mid = (u + d) // 2
            if target < matrix[mid][0]:
                d = mid - 1
            elif target > matrix[mid][-1]:
                u = mid + 1
            else:
                break

        if u > d:
            return False
        mid = (u + d) // 2
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            col = (l + r) // 2
            if target < matrix[mid][col]:
                r = col - 1
            elif target > matrix[mid][col]:
                l = col + 1
            else:
                return True
        return False