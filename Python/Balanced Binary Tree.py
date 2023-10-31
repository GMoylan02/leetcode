# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return dfs(root)[0]


def dfs(root):
    if not root:
        return [True, 0]

    l, r = dfs(root.left), dfs(root.right)
    if l[0] and r[0] and abs(l[1] - r[1]) <= 1:
        return [True, 1 + max(l[1], r[1])]
    else:
        return [False, 1 + max(l[1], r[1])]



