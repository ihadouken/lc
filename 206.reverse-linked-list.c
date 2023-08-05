/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
typedef struct ListNode Node;

/* Approach: Recursion, Complexity: O(n), O(n) */
// Node* reverseList(Node* head){
//     /* Keep recursing till the last node (or if the list is empty). */
//     if (!head || !head->next)
//         return head;
//
//     Node* newhead;
//     /* When the recursive calls start to return back, they propagate a pointer
//      * to the last node in the input which is required as the head of the new
//      * reversed linked list.
//      */
//     newhead = reverseList(head->next);
//
//     /* Reverse the link of the node next to current head. */
//     head->next->next = head;
//     /* Make current head node to point NULL for now as we don't know if there
//      * are nodes to its left. If there is a node to its left, head->next will
//      * be reinitialized to point it.
//      */
//     head->next = NULL;
//
//     /* Pass pointer to last node (in the original list) to parent function call
//      * as discussed above.
//      */
//     return newhead;
// }

/* Approach: Three Pointer, Complexity: O(n), O(1) */
Node* reverseList(Node* head){
    Node *prev, *cur, *next;
    prev = NULL;
    cur = head;

    /* Stop after processing the last node. */
    while (cur) {
        /* Store the next node and set the previous node as new next. */
        next = cur->next;
        cur->next = prev;

        /* Move the pointers forward i.e. processed node is previous for next node.
         * node next to processed node is processed in subsequent iteration.
         */
        prev = cur;
        cur = next;
    }

    /* Return old list's last node as new list's head. */
    return prev;
}
