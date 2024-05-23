# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorderTraversal(root,res) :
            if root is None:
                return None
            inorderTraversal(root.left,res)
            res.append(root.val)
            inorderTraversal(root.right,res)
            
        res=[]
        inorderTraversal(root, res)
        return res[k-1]
        