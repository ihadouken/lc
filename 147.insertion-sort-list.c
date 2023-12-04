/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
typedef struct ListNode Node;

/* Approach: Two Pointer, Complexity: O(n^2), O(1) */
Node* insertionSortList(Node* head){
    Node dummy, *pivot, *last, *cur;
    /* Use a dummy node to keep track of varying head and handle edge cases. */
    dummy.next = head;

    /* "pivot" -> node to be added in sorted sublist i.e. pivot. */
    pivot = head->next;

    /* "last" -> last node in sorted sublist. */
    last = head;

    /* Keep adding nodes (pivots) to sorted sublist until there are none left. */
    while (pivot) {
        /* If the pivot belongs at the end of sorted sublist. */
        if (last->val <= pivot->val) {
            last = last->next;
            pivot = pivot->next;
            continue;
        }

        /* Find node which should be before pivot node in sorted sublist. */
        cur = &dummy;
        while (cur->next->val <= pivot->val)
            cur = cur->next;

        /* Move the pivot from its original position to sorted position. */
        last->next = pivot->next;
        pivot->next = cur->next;

        /* Link the found node (maximum smaller than pivot) to pivot. */
        cur->next = pivot;

        /* Process the next node in unsorted sublist as pivot. */
        pivot = last->next;
    }

    /* Return pointer to head of sorted list. */
    return dummy.next;
}

/* Approach: Array + Sorting, Complexity: O(n^2), O(n) */
// Node* insertionSortList(Node* head){
//     int length, pivot, i, j;
//     Node* cur;
//
//     /* Find the length of list to know required size of array. */
//     cur = head;
//     length = 0;
//
//     while (cur) {
//         cur = cur->next;
//         ++length;
//     }
//
//     /* Allocate array to store and sort node values. */
//     int *list = (int*) malloc(sizeof(int) * length);
//     cur = head;
//
//     /* Copy node values into the auxillary array. */
//     for (i = 0; i < length; ++i) {
//         list[i] = cur->val;
//         cur = cur->next;
//     }
//
//     /* Sort the array containing node values via insertion sort. */
//     for (i = 1; i < length; ++i) {
//         pivot = list[i];
//
//         for (j = i-1; j >= 0; --j) {
//             if (list[j] > pivot)
//                 list[j+1] = list[j];
//             else
//                 break;
//         }
//
//         list[j+1] = pivot;
//     }
//
//     /* Write node values into the list (from the array) in sorted order. */
//     cur = head;
//     for (i = 0; i < length; ++i) {
//         cur->val = list[i];
//         cur = cur->next;
//     }
//
//     /* Return the modified list. */
//     return head;
// }
