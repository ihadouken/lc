/* Comparator for quicksort. Selects who comes first in a sorted array via
 * its returned value.
 * Case I (-ve): Element at x precedes element at y in the sorted array.
 * Case II (+ve): Element at x succeeds element at y in the sorted array.
 * Case III (0): Element at x is equal to y. It may succeed or precede it. */
int cmp(void* x, void* y) {
    int n1, n2;
    n1 = *((int*) x);
    n2 = *((int*) y);

    return n1 - n2;
}

/* Approach: Sorting, Two Pointer, Greedy.
 * Complexity: O(nlogn), O(1)
 * Method: Sort the people weight-wise. Maximum two people can sit in a boat.
 *         Thus the problem reduces to selection of most optimal pair at each
 *         iteration like Two Sum II (#167). Therefore, it is greedy as we
 *         select locally optimal pairs and that leads us to the solution. */

int numRescueBoats(int* people, int peopleSize, int limit){
    /* Library QuickSort */
    qsort(people, peopleSize, sizeof(int), cmp);

    int l, r, boats;
    /* When sorted, the leftmost and rightmost are most likely to fit together
     * perfectly into the limit. */
    l = 0;
    r = peopleSize - 1;
    boats = 0;

    while (l < r) {
        /* If their sum exceeds limit, put the heavier weight into the boat as
         * it is wont find an optimal match as it is already with the lowest
         * weight possible. However, the lighter weight can find a better
         * weight to the left of the heavier weight. This is due to sorted
         * nature of the input. */
        if (people[l] + people[r] > limit)
            r--;

        /* If the sum doesn't exceed limit, we found an optimal pair i.e. the
         * heaviest available weight has been coupled with the lightest available
         * weight. We may put both into one boat. */
        else {
            l++;
            r--;
        }
        boats++;
    }

    /* When only one element is left, no pairing is possible. Put this one into
     * its own boat. */
    if (l == r)
        boats++;
    return boats;
}
