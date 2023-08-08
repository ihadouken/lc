/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
typedef struct ListNode Node;

/* Approach: Two Pointer, Complexity: O(n), O(1) */
/* Tip: Shift all unique nodes to a sublist beginning at the start of the list
 *      via two pointer then delete the sublist containing rest of the nodes.
 */

/* Delete an entire list (or sublist terminating at end) from heap memory. */
void free_list(Node* head) {
    Node* del;
    while (head) {
        del = head;
        head = head->next;
        free(del);
    }
}

Node* deleteDuplicates(Node* head){
    /* No duplicates in lists of size < 2. */
    if (!head || !head->next)
        return head;

    /* Pointer i always points at end of sublist with all unique elements,
     * j points at node under processing and jprev points at node just before
     * j. jprev is required to check if the current node is a duplicate.
     * Since the first node is always unique, i starts from the first node and
     * j starts from the second node.
     */
    Node *i, *j, *jprev;
    i = jprev = head;
    j = head->next;

    while (j) {
        /* If a unique node is found append it to the unique node sublist. */
        if (j->val != jprev->val){
            i = i->next;
            i->val = j->val;
        }
        /* Ignore the duplicate node. */
        j = j->next;
        jprev = jprev->next;
    }

    /* All nodes after the unique node sublist are duplicates and are deleted. */
    free_list(i->next);

    /* Define new end of the linked list just after the unique node list. */
    i->next = NULL;
    return head;
}
