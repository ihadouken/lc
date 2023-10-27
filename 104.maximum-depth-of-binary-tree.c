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

/* Approach: DFS + Recursion, Complexity:  O(n), O(n) */
int maxDepth(struct TreeNode* root){
    /* If there is node, the path below haas no depth. */
    if (!root)
        return 0;

    /* Get max length path below a node by selecting the larger of the left and 
     * right paths. Add 1 to account for the node itself. */
    return max(maxDepth(root->left), maxDepth(root->right)) + 1;
}
