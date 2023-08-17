/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
typedef struct ListNode Node;

/* Approach: In-Place Operations, Complexity: O(n), O(1) */
/* Tip: To delete a node in a linked list, the nodes before and after it are
 * required. As the node before the target node can't be reached, shift the
 * values of each node after the target node to the left and then delete the
 * tail node. This ends up overwriting the target node with the node to its
 * right. After shifting, there is one extra node at the end which is deleted.
 */
void deleteNode(Node* node) {
    Node* prev;
    while (node->next) {
        node->val = node->next->val;
        prev = node;
        node = node->next;
    }

    prev->next = NULL;
    free(node);
}
