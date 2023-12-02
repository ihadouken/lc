/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
typedef struct ListNode Node;

/* Approach: Slow/Fast Pointers, Complexity: O(n), O(1) */
Node *detectCycle(Node *head) {
    /* List with 0 or 1 nodes with NULL at end can't have a cycle. */
    if (!head || !head->next)
        return NULL;

    /* Use slow/fast pointers to detect a cycle. */
    Node *slow, *fast;
    slow = head->next;
    fast = head->next->next;

    while (slow != fast) {
        /* If a terminal (NULL) is encountered, no cycle exists. */
        if (!fast || !fast->next)
            return NULL;
        slow = slow->next;
        fast = fast->next->next;
    }

    /* d(fast) = 2 * d(slow) -> Z + a + nC = 2*Z + 2*a -> C = Z+a -> Z = C-a */
    slow = head;

    /* The intersection point (a) of the cycle (C) is as many nodes away from cycle
     * entry (C-a) as there are nodes outside the cycle starting from head (Z).
     */
    while (slow != fast) {
        slow = slow->next;
        fast = fast->next;
    }

    /* The next intersection occurs when one pointer continues the cycle while
     * another restarts from head. Both pointers have same speed of one node.
     * This intersection (as signified by the above math) is the cycle entry.
     */
    return slow;
}
