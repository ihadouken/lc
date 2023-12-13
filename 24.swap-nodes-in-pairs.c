/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
typedef struct ListNode Node;

/* Approach: Two Pointer, Complexity: O(n), O(1) */
Node* swapPairs(Node* head){
    /* Trivial case: Input needs no processing. So, return as is. */
    if (!head || !head->next)
        return head;

    /* Head of the output list = Second node of input list.*/
    Node *newhead, *next;
    newhead = head->next;

    /* Stop until no or only one node is left i.e. no pairs left. */
    while (head && head->next) {
        /* Reverse the link of the node after to head as it appears before head
         * in the output. Before doing this, save the link to the first node in
         * the next pair i.e. head->next->next as it is to be processed next.
         */
        next = head->next->next;
        head->next->next = head;

        /* If next is the terminal or the last node, link head to it as no pairs
         * are left. Otherwise, link head to node after next. Because if next and
         * next->next are to be swapped, next->next occurs prior to next in output.
         */
        if (!next || !next->next)
            head->next = next;
        else
            head->next = next->next;

        /* Move head to process next pair of nodes. */
        head = next;
    }

    return newhead;
}
