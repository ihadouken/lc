/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
typedef struct ListNode Node;

/* Reverse a linked list (or sublist) starting at given node till end. */
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
void reorderList(struct ListNode* head){
    /* Use dummy node to get left (desired) midpoint for even lists. */
    Node dummy, *slow, *fast, *part1, *part2, *next1, *next2;
    dummy.next = head;
    slow = fast = &dummy;

    /* Slow/Fast pointers to find the mid of the linked list. */
    while (fast && fast->next) {
        fast = fast->next->next;
        slow = slow->next;
    }

    /* Split the list after middle node and reverse the second part. */
    part1 = head;
    part2 = reverse(slow->next);
    slow->next = NULL;

    /* Merge the two parts using alternate nodes from both lists. Stop if either
     * of the lists exhaust i.e. no more nodes to merge. */
    while (part1 && part2) {
        /* Store the next of nodes to be merged for future use. */
        next1 = part1->next;
        next2 = part2->next;

        /* Firts part's node is linked to second part's node. */
        part1->next = part2;
        /* The second part's node is linked to the next node in the first part. */
        part2->next = next1;

        /* Move pointers to merge next nodes in first and second part. */
        part1 = next1;
        part2 = next2;
    }

    /* Return the new (modified) list after the merging. */
    return head;
}
