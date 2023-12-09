/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
typedef struct ListNode Node;

/* Approach: Two Pointers, Complexity: O(n) (single pass), O(1) */
Node* removeNthFromEnd(Node* head, int n){
    int diff;
    Node *l, *r, *del;
    l = r = head;
    diff = 0;

    /* Move right till it points to the last node. */
    while (r->next != NULL) {
        if (diff < n)
            ++diff;
        /* Start moving left when it is n nodes behind right. */
        else
            l = l->next;
        r = r->next;
    }

    /* Corner case: Last node from the right is to be removed i.e. head.
     *              In this case, left is one less than n nodes behind right.
     */
    if (diff == n-1) {
        del = head;
        head = head->next;
    }
    /* Left now points to the node just behind the one to be deleted. Mark the
     * node next to it for deletion. Now update its next pointer such that it
     * ends up bypassing the marked node in the new list.
     */
    else {
        del = l->next;
        l->next = l->next->next;
    }

    /* Delete the node marked for deletion and return head of new list. */
    free(del);
    return head;
}
