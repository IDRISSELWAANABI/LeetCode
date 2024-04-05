class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        result = []
         
        
        left_subtree = self.postorderTraversal(root.left)  
        right_subtree = self.postorderTraversal(root.right) 
        
        result.extend(left_subtree)  
        result.extend(right_subtree)  
        result.append(root.val) 
        
        return result