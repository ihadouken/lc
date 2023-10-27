/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int max(int x, int y) {
    if (x > y)
        return x;
    return y;
}

int abs(int x) {
    if (x < 0)
        return x * -1;
    return x;
}

/* Recursively check if all subtrees are balanced. */
int depth(struct TreeNode* root, bool* res) {
    /* Nulls amount to zero depth. */
    if (!root)
        return 0;

    /* Find depths of left and right subtrees. */
    int ldepth, rdepth;
    ldepth = depth(root->left, res);
    rdepth = depth(root->right, res);

    /* Check if subtree is balanced using definition. */
    if (abs(ldepth-rdepth) > 1)
        *res = false;

    /* depth of binary tree = depth of larger of left and right subtrees + 1. */
    return max(ldepth, rdepth) + 1;
}

/* Approach: DFS + Recursion, Complexity: O(n), O(n) */
bool isBalanced(struct TreeNode* root){
    /* Boolean to be writable by all recursive calls. */
    bool res;
    /* Initially, assume the tree is balanced. */
    res = true;

    depth(root, &res);
    /* If no node finds its left and right subtrees unbalanced, res remains true. */
    return res;
}
