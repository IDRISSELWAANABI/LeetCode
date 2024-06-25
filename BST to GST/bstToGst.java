class Solution {
    public TreeNode bstToGst(TreeNode root) {
        reverse_in_order(root,0);
        return root ; 

        
    }
    private int reverse_in_order(TreeNode node , int acc){
        if(node == null){
            return acc;
        }
        acc=reverse_in_order(node.right,acc);
        acc+=node.val ;
        node.val = acc ; 
        acc=reverse_in_order(node.left,acc) ; 
        return acc ; 
    }
}