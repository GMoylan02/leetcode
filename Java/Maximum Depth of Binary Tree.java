/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null){
            return 0;
        }
        return depth(root, 1);
    }
    public int depth(TreeNode root, int current){
        if (root.left == null && root.right == null){
            return current;
        }
        if (root.left == null){
            return depth(root.right, current+1);
        }
        if (root.right == null){
            return depth(root.left, current+1);
        }
        return Math.max(depth(root.left, current+1), depth(root.right, current+1));
    }
}