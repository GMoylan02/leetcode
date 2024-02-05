# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(root, l: Optional[int], r: Optional[int]):
            if not root:
                return True
            if not l < root.val < r:
                return False
            return validate(root.left, l, root.val) and validate(root.right, root.val, r)

        return validate(root, float('-inf'), float('inf'))
