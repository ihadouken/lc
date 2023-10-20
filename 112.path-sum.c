/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

/* Approach: DFS + Recursion, Complexity: O(n), O(n) */
bool hasPathSum(struct TreeNode* root, int targetSum){
    /* Corner Case: No paths in empty tree. */
    if (!root)
        return false;

    /* Base Case: Leaf node i.e. no children. */
    if (!root->left && !root->right) {
        /* If the path has required sum, propagate a true back to the root. */
        if (targetSum == root->val)
            return true;
        /* Else, propagate a false to parent node. */
        return false;
    }

    /* Required target reduces by root->val for any path down the node. */
    targetSum -= root->val;

    /* Either left OR right path from the current node can be the desired path. */
    return (root->left && hasPathSum(root->left, targetSum)) || (root->right && hasPathSum(root->right, targetSum));
}
