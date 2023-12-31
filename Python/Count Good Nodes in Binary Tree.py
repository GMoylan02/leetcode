# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def count(root, current_max):
            if not root:
                return 0
            if root.val >= current_max:
                return 1 + count(root.left, root.val) + count(root.right, root.val)
            else:
                return 0 + count(root.left, current_max) + count(root.right, current_max)

        return 1 + count(root.left, root.val) + count(root.right, root.val)