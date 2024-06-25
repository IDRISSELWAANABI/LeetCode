class Solution {
public:
    TreeNode* bstToGst(TreeNode* root) {
        reverseInOrder(root, 0);
        return root;
    }

private:
    int reverseInOrder(TreeNode* node, int acc) {
        if (node == nullptr) {
            return acc;
        }
        acc = reverseInOrder(node->right, acc);
        acc += node->val;
        node->val = acc;
        acc = reverseInOrder(node->left, acc);
        return acc;
    }
};
