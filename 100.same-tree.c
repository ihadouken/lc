/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

/* Approach: DFS + Recursion, Complexity: O(n), O(n) */
/* Tip: Two trees are the same if all of their corresponing subtrees are same. */

bool isSameTree(struct TreeNode* p, struct TreeNode* q){
    /* Paths in same trees terminate simultaneously and nodes have equal values. */
    if (!p && !q)
        return true;
    else if (!p ^ !q || p->val != q->val)
        return false;

    /* Corresponding left and right subtrees must be same. */
    return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
}
