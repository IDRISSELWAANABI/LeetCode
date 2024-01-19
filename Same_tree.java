class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }
    
   class Solution {
       public boolean isSameTree(TreeNode p, TreeNode q) {
           if (p == null && q == null){
               return true ; 
           }
           if (p == null || q == null){
               return false ; 
           }
           return p.val == q.val && this.isSameTree(p.left, q.left) && this.isSameTree(p.right, q.right);
           
       }
   }