/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
typedef struct ListNode Node;

/* Approach: Two Pointer + Slow/Fast Pointers, Complexity: O(n), O(1) */
bool isPalindrome(Node* head){
    Node *slow, *fast, *prev, *cur, *next, *tail;
    slow = fast = head;

    /* Use Slow/Fast Pointers to find the middle of the list. For lists of even
     * length, middle means the first node in the second half.
     */
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }

    /* Reverse the list from mid to last node (both inclusive) via 3 pointers.
     * Reversal of second half enables us to traverse it in the opposite way.
     * Both parts of the list will share the middle element.
     * Odd: 1 -> 2 -> 3 -> 4 -> 5 -> X becomes 1 -> 2 -> 3 <- 4 <- 5 (with 3
     *      points to NULL)
     * Even: 1 -> 2 -> 3 -> 4 -> X becomes 1 -> 2 -> 3 <- 4 (3 points NULL)
     */
    prev = NULL;
    cur = slow;
    while (cur) {
        next = cur->next;
        cur->next = prev;

        prev = cur;
        cur = next;
    }

    /* Two pointers move towards the middle from opposite ends. This checks if
     * the first half (pointed by head) equals the reverse of the second half
     * (pointed by tail). Since even length list contains one extra node in the
     * first half, check if tail points to NULL for termination rather than head.
     */
    tail = prev;
    while (tail)  {
        if (head->val != tail->val)
            return false;
        head = head->next;
        tail = tail->next;
    }

    return true;
}
