#define OPEN '['
#define CLOSE ']'

/* Approach: Two Pointers + Greedy, Complexity: O(n), O(1) */
int minSwaps(char * s){
    int swaps, l, r, lcount, rcount;
    swaps = lcount = rcount = 0;
    l = 0;
    r = strlen(s) - 1;

    /* Run two pointers one on each end. Keep a count on each end of string.
     * In balanced string, enough openings must exist to left of endings and
     * vice verse. If the count reaches -1 on one side, a swap has to be made.
     * Keep this pointer on hold and wait for the count on other side reach -1.
     * When count reaches -1 on both sides, we make a swap.
     *
     * Pointers are positioned at far ends to maximise substring between swapped
     * ends. This way maximum characters will comprise a balanced substring after
     * the swap via Rule 3.
     */
    while (l < r) {
        /* Don't modify sum while a pointer is fixed while at count -1. */
        if (lcount != -1) {
            if (s[l] == OPEN)
                lcount++;
            else
                lcount--;
        }

        if (rcount != -1) {
            if (s[r] == CLOSE)
                rcount++;
            else
                rcount--;
        }

        if (lcount == -1 && rcount == -1) {
            swaps++;
            /* Change count from -1 -> 1 as if we had seen an opening on the
             * left and a closing on the right.
             */
            l++;
            lcount = 1;
            r--;
            rcount = 1;
        }
        else if (lcount == -1) {
            r--;
        }
        else if (rcount == -1) {
            l++;
        }
        else {
            l++;
            r--;
        }
    }
    return swaps;
}
