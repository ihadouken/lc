/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
typedef struct ListNode Node;

/* Approach: Slow/Fast Pointers, Complexity: O(n), O(1) */
/* Use Floyd's tortoise and hare cycle detection algorithm. If two pointers are
 * traversing a loop at different speeds, they must meet at some point eventually
 * i.e. fast pointer will eventually catch up to the slow pointer after being
 * ahead of it by distance of 1 cycle length.
 */
bool hasCycle(Node *head) {
    Node *fast, *slow;
    slow = fast = head;
    
    /* Since fast moves two nodes per iteration, so it reaches the end first.
     * Ensure it is not NULL or the last node. This also covers corner cases
     * like empty list, list with 1 non-cyclic node etc.
     */
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;

        if (fast == slow)
            return true;
    }

    /* If fast never met slow but instead reached the end, there is no cycle. */
    return false;
}
