# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return helper(root, 0)


def helper(root, old_max):
    if not root:
        return old_max
    new_max = max(max_depth(root.left) + max_depth(root.right), old_max)
    return max(helper(root.left, new_max), helper(root.right, new_max))


def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))