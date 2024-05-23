class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def isValidRoot(node, min_val=float('-inf'), max_val=float('inf')):
            if not node:
                return True
            
            if not (min_val < node.val < max_val):
                return False

            return (
                isValidRoot(node.left, min_val, node.val) and
                isValidRoot(node.right, node.val, max_val)
            )

        return isValidRoot(root)
