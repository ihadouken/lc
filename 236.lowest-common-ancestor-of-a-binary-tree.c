/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
typedef struct TreeNode Node;

/* Approach: DFS + Recursion, Complexity: (n), O(h) */
Node* lowestCommonAncestor(Node* root, Node* p, Node* q) {
    /* If neither p or q are found in a path, propagate NULL until one of them
     * is found.
     */
    if (!root)
        return NULL;

    /* Try to find p and q in both subtrees of "root". */
    Node *left, *right;
    left = lowestCommonAncestor(root->left, p, q);
    right = lowestCommonAncestor(root->right, p, q);

    /* Both p and q are found in separate subtrees of LCA (or the LCA must be one
     * of them).
     */
    if ((left && right) || root->val == p->val || root->val == q->val)
        return root;

    /* Propagate the LCA up to root node i.e. 1st call to function. */
    else if (left)
        return left;
    else if (right)
        return right;

    /* If both subtrees dont contain p or q, return NULL. (impossible by constraints) */
    return NULL;
}
