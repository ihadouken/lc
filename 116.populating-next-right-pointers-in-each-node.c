/**
 * Definition for a Node.
 * struct Node {
 *     int val;
 *     struct Node *left;
 *     struct Node *right;
 *     struct Node *next;
 * };
 */
typedef struct Node Node;

/* Approach: Two Pointers + DFS (modified), Complexity: O(n), O(1) */
/* Tip: Use connected nodes in the previous level to connect nodes in a level. */
Node* connect(Node* root) {
    /* Nothing to connect in an empty tree. */
    if (!root)
        return NULL;

    Node *prev, *cur, *curcopy;
    prev = root;
    cur = root->left;

    /* Iterate over the tree one level at a time. */
    while (cur) {
        /* Connect the 1st and 2nd nodes in a level via their parent i.e. 1st node in prev. level. */
        curcopy = cur;
        cur->next = prev->right;
        cur = cur->next;
        prev = prev->next;

        /* Connect nodes in current level via their parents in the prev. level. */
        while (prev) {
            cur->next = prev->left;
            cur = cur->next;
            cur->next = prev->right;
            cur = cur->next;
            prev = prev->next;
        }

        /* Move on to connecting the next level. */
        prev = curcopy;
        cur = prev->left;
    }

    /* Return the tree with adjacent nodes connected. */
    return root;
}
