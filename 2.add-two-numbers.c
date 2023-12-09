/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
typedef struct ListNode Node;

/* Approach: Math, Complexity: O(m+n), O(1) */
Node* addTwoNumbers(Node* l1, Node* l2){
    /* Store dummy node in stack as its not required to be persistant. */
    Node dummy;
    Node *l3;
    int sum, carry;

    /* Use dummy node to avoid initializing first element of l3 in the loop. */
    l3 = &dummy;
    carry = 0;

    /* Continue until both lists are exhausted and there is no previous carry. */
    while (carry || l1 || l2) {
        sum = carry;
        if (l1) {
            sum += l1->val;
            l1 = l1->next;
        }
        if (l2) {
            sum += l2->val;
            l2 = l2->next;
        }

        /* Store next sum digit in a new node allocated in the heap and link it
         * to the previous node. Always point to the last stored digit to link
         * it in future to the next one.
         */
        l3 = l3->next = (Node*) malloc(sizeof(Node));
        l3->val = sum % 10;

        /* Compute carry for next digit column of sum. */
        carry = sum / 10;
    }

    /* Terminate list containing sum digit. Return pointer to its first element. */
    l3->next = NULL;
    return dummy.next;
}
