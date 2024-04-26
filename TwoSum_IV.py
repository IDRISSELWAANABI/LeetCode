class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)

        numbers = inorder(root)
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] < k:
                l += 1
            elif numbers[l] + numbers[r] > k:
                r -= 1
            else:
                return True
        return False