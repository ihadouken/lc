/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
typedef struct ListNode Node;

/* Approach: Slow/Fast Pointers, Complexity: O(n), O(1) */
/* Tip: When one pointer moves half as fast as the other, it only covers half
 *      the distance while the faster one reaches the end.
 */
Node* middleNode(Node* head){
    Node *slow, *fast;
    slow = fast = head;

    /* Keep traversing till fast pointer reaches last node or the sentinel (NULL). */
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }

    return slow;
}
