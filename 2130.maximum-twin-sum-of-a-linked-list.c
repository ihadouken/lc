/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
typedef struct ListNode Node;

/* Return max of two integers. */
int max(int x, int y) {
    if (x > y)
        return x;
    return y;
}

/* Reverse a linked list (or sublist) starting at given node. */
Node* reverse(Node* head) {
    Node *prev, *cur, *next;
    prev = NULL;
    cur = head;

    while (cur) {
        next = cur->next;
        cur->next = prev;

        prev = cur;
        cur = next;
    }

    return prev;
}

/* Approach: Two Pointer, Complexity: O(n), O(1) */
int pairSum(Node* head){
    int maxsum, twinsum;
    Node dummy, *slow, *fast, *part1, *part2;
    maxsum = 0;
    dummy.next = head;
    slow = fast = &dummy;

    /* Find the middle of the list (left one for even length lists). */
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }

    /* Split the list into two parts and reverse the second half. */
    part1 = head;
    part2 = reverse(slow->next);
    slow->next = NULL;

    /* Iterate over both parts simultaneously to examine each twin sum. */
    while (part1) {
        twinsum = part1->val + part2->val;
        maxsum = max(maxsum, twinsum);

        part1 = part1->next;
        part2 = part2->next;
    }

    /* Return the maintained maximum twin sum. */
    return maxsum;
}
