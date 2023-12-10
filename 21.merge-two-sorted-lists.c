/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
typedef struct ListNode Node;

/* Approach: Greedy, Complexity: O(n), O(1) */
/* See below for a more readable implementation. */
Node* mergeTwoLists(Node* list1, Node* list2){
    /* Set defaults for head and tail of output list (after merging). */
    Node *newhead, *newtail;
    newtail = newhead = NULL;

    /* Keep processing until there are nodes to be merged. At all times list1
     * points to next node to be added from first list and list2 points to next
     * node to be added from second list. Make a local decision about which node
     * to select out of two nodes (pointed by list1 and list2).
     */
    while (list1 || list2) {
        /* Add node from list1 if its smaller than list2 node or if list2 is
         * exhausted.
         */
        if (!list2 || (list1 && list1->val < list2->val)) {
            /* Append to output linked list. */
            if (newtail)
                newtail = newtail->next = list1;
            /* Initialize the output's first node. */
            else
                newtail = newhead = list1;
            /* Now consider next node from list1. */
            list1 = list1->next;
        }
        /* Add node from list2 if its smaller than list1 node or if list1 is
         * exhausted.
         */
        else {
            /* Append to output linked list. */
            if (newtail)
                newtail = newtail->next = list2;
            /* Initialize the output's first node. */
            else
                newtail = newhead = list2;
            /* Now consider next node from list2. */
            list2 = list2->next;
        }
    }

    return newhead;
}

// Node* mergeTwoLists(Node* list1, Node* list2){
//     /* If any of the lists is empty, return the other. Works if both are empty. */
//     if (!list1)
//         return list2;
//     if (!list2)
//         return list1;
//
//     /* Set the head of output list. */
//     Node *newhead, *newtail;
//     if (list1->val < list2->val) {
//         newhead = newtail = list1;
//         list1 = list1->next;
//     }
//     else {
//         newhead = newtail = list2;
//         list2 = list2->next;
//     }
//
//     /* Make local decisions about which list to add node from until one of the
//      * lists is exhausted.
//      */
//     while (list1 && list2) {
//         if (list1->val < list2->val) {
//             newtail = newtail->next = list1;
//             list1 = list1->next;
//         }
//         else {
//             newtail = newtail->next = list2;
//             list2 = list2->next;
//         }
//     }
//
//     /* Link the tail of the output list to whichever list which is not exhausted. */
//     if (list1)
//         newtail->next = list1;
//     else
//         newtail->next = list2;
//
//     return newhead;
// }
