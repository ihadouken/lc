/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
typedef struct TreeNode Node;

/* Approach: Binary Search + DFS, Complexity: O(logn), O(1) */
Node* lowestCommonAncestor(Node* root, Node* p, Node* q) {
    /* Ensure p is the smaller node and q is the bigger one. */
    if (p->val > q->val)
        return lowestCommonAncestor(root, q, p);

    /* Continue until current node is between (or equal to) p and q in the BST. */
    while (root->val < p->val || root->val > q->val) {
        /* If both p and q are smaller than current, search left subtree. */
        if (root->val > q->val)
            root = root->left;
        /* If both p and q are greater than current, search right subtree. */
        else
            root = root->right;
    }

    /* Return the first node >= p and <= q. Equality is considered as a node can 
     * be its own descendant.
     */
    return root;
}
