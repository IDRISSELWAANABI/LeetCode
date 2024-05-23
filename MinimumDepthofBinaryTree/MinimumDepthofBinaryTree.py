# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root) :
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        left_depth = float('inf') if root.left is None else self.minDepth(root.left)
        right_depth = float('inf') if root.right is None else self.minDepth(root.right)
        return min(left_depth, right_depth) + 1
