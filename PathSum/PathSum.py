class Solution {
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if (root == null){
            return false;
        }
        if (root.left == null && root.right == null){
            return root.val == targetSum ; 
        }
        boolean left_sum = hasPathSum(root.left, targetSum - root.val);
        boolean right_sum = hasPathSum(root.right, targetSum - root.val);
        return left_sum || right_sum;
        
    }
}