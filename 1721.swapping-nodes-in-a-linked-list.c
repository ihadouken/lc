/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
typedef struct ListNode Node;

void swap(int* x, int* y) {
    int temp;
    temp = *x;
    *x = *y;
    *y = temp;
}

/* Approach: Two Pointer, Complexity: O(n) (single pass), O(1) */
Node* swapNodes(Node* head, int k){
    int i;
    Node *kth, *kth_last, *cur;

    /* Get kth node by traversing k-1 nodes from the head. */
    kth = head;
    for (i = 1; i < k; ++i)
        kth = kth->next;

    /* Use a second pointer (starting from head) and move it n-k times to reach
     * the kth node from last. To do this in one pass, move it as many times as
     * a pointer starting from kth node (already found) to last node has to move.
     */
    kth_last = head;
    cur = kth;
    while (cur->next) {
        cur = cur->next;
        kth_last = kth_last->next;
    }

    /* Swap values for kth node from start and end. Return pointer to list. */
    swap(&kth_last->val, &kth->val);
    return head;
}
