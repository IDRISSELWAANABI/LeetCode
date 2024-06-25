class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def reverse_in_order(node, acc):
            if not node:
                return acc
            acc = reverse_in_order(node.right, acc)
            acc += node.val
            node.val = acc
            acc = reverse_in_order(node.left, acc)
            return acc

        reverse_in_order(root, 0)
        return root
