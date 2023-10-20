/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

/* Approach: DFS + Recursion, Complexity: O(n), O(n) */

void invert(struct TreeNode* root) {
    /* Base Case: Path ran out of nodes. */
    if (!root)
        return;

    /* Find memory locations pointed by left and right. */
    long left, right;
    left = root->left;
    right = root->right;

    /* Make right child point to past left child. */
    root->right = left;
    /* Make left child point to past right child. */
    root->left = right;

    /* Recurse for left subtree. */
    invert(root->left);
    /* Recurse for right subtree. */
    invert(root->right);
}

struct TreeNode* invertTree(struct TreeNode* root){
    /* Initiate recursive algorithm on root. */
    invert(root);
    /* Return the root after modifications. */
    return root;
}
