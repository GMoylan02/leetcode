# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        def recurse(root, depth):
            if not root:
                return
            if not len(result) < depth:
                result.append([])
            result[depth].append(root.val)
            recurse(root.left, depth+1)
            recurse(root.right, depth+1)

        result = []
        if not root:
            return result
        recurse(root, 0)
        return [ele for ele in result if ele != []]