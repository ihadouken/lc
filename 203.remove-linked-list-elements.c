/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
typedef struct ListNode Node;

void free_list(Node* head) {
    Node* next;
    while (head) {
        next = head->next;
        free(head);
        head = next;
    }
}

/* Approach: Two Pointer, Complexity: O(n), O(1) */
Node* removeElements(Node* head, int val){
    /* Use dummy node for edge case where all nodes contain "val". Use separate
     * pointers to read from and write to the list.
     */
    Node dummy, *last, *read, *write;
    dummy.next = head;
    read = write = head;
    last = &dummy;

    while (read) {
        /* Only values other than "val" are written to the list. */
        if (read->val != val) {
            write->val = read->val;
            last = last->next;
            write = write->next;
        }
        /* Move "read" to the next node to read its value. */
        read = read->next;
    }

    /* As the output has "last" as the last node, terminate the list after "last".
     * Delete all nodes after the new last node as they are useless. */
    free_list(last->next);
    last->next = NULL;

    /* Dummy always points to the head of the output list. */
    return dummy.next;
}
