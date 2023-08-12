/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
typedef struct ListNode Node;

/* Approach: Two Pointer, Complexity: O(n), O(1) */
Node* oddEvenList(Node* head){
    /* For empty list, single node list and double node list, input is already
     * equal to result.
     */
    if (!head || !head->next || !head->next->next)
        return head;

    /* Start 'odd' from the first odd node and 'even' from first even node. */
    Node *evenhead, *even, *odd;
    odd = head;
    even = evenhead = head->next;

    /* Link all odd nodes (in order) together. Do the same for even nodes. The
     * even nodes always run out first. So for termination, check if 'even'
     * points to NULL or last node in the list i.e. no more nodes left to link.
     */
    while (even && even->next) {
        odd->next = odd->next->next;
        odd = odd->next;
        even->next = even->next->next;
        even = even->next;
    }

    /* Link the last odd node with first even node and output the resultant list. */
    odd->next = evenhead;
    return head;
}
