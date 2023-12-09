int min(int x, int y) {
    if (x < y)
        return x;
    return y;
}

int cmp(void *x, void *y) {
    return *((int*) x) - *((int*) y);
}

/* Approach: Sorting + Sliding Window, Complexity: O(nlogn), O(1) */
int minimumDifference(int* nums, int numsSize, int k){
    /* No scores to consider. */
    if (!numsSize)
        return 0;

    /* Sort the input so that subsequent scores are higher. Also when sorted,
     * the difference between two element in the list is a function of their
     * separation.
     */
    qsort(nums, numsSize, sizeof(int), cmp);

    int l, r, diff;
    /* Difference between ends of window (of size <= n) can't be higher than the
     * difference of global maxima and minima in the input. Hence, the default.
     */
    diff = nums[numsSize-1] - nums[0];

    /* Point to the ends of a window of size k using two pointers. */
    l = 0;
    r = k-1;

    while (r < numsSize) {
        /* Check if this window is more optimal. If yes, store its difference. */
        diff = min(diff, nums[r] - nums[l]);
        /* Move both pointers to consider next window of size k. */
        ++r;
        ++l;
    }

    return diff;
}
