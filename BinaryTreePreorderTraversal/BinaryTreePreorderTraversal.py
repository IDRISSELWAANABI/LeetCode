# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        result = []
        result.append(root.val)  
        
        left_subtree = self.preorderTraversal(root.left)  
        right_subtree = self.preorderTraversal(root.right) 
        
        result.extend(left_subtree)  
        result.extend(right_subtree)  
        
        return result
