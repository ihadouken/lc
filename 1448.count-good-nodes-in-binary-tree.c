/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
typedef struct TreeNode Node;

int max(int x, int y) {
    if (x > y)
        return x;
    return y;
}

/* Recursive function to return count of good nodes. */
int dfs(Node* cur, int pathmax) {
    /* Null can't be a good node so increment count by 0. */
    if (!cur)
        return 0;

    /* Increment count by 1 if max in path doesn't exceed current node's value.
     * Check (and possibly increment count) recursively for the node's children
     * with an updated path maximum.
     */
    return (pathmax <= cur->val) + dfs(cur->left, max(pathmax, cur->val)) + dfs(cur->right, max(pathmax, cur->val));
}

/* Approach: DFS + Recursion, Complexity: O(n), O(n) */
/* Tip: Use DFS to traverse every path. Good node has no node with value > its
 *      value in the path from root to it.
 */
int goodNodes(Node* root){
    /* Initiate DFS on root node with minimum possible path maximum. */
    return dfs(root, INT_MIN);
}
