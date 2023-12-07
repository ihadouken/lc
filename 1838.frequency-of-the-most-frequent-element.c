int cmp(void* x, void* y) {
    return *((int*) x) - *((int*) y);
}

int max(int x, int y) {
    if (x > y)
        return x;
    return y;
}

/* Approach: Sorting + Sliding Window, Complexity: O(nlogn), O(1) */
int maxFrequency(int* nums, int numsSize, int k){
    long winsum;
    int l, r, res;

    /* Sort input so that when trying to max possible frequency of a particular
     * element, all elements incrementable to equal the element are conveniently
     * placed to its left.
     */
    qsort(nums, numsSize, sizeof(int), cmp);
    res = winsum = 0;

    /* Append elements to the right end of window one at a time. */
    for (l = r = 0; r < numsSize; ++r) {
        /* Maintain the sum of elements currently in the window. */
        winsum += nums[r];

        /* Window is invalid if the no. of operations required > no. of operations
         * available. Evict the element consuming most operations i.e. smallest
         * element (present at window's left end) until it is valid again.
         */
        while (l < r && (long) nums[r]*(r-l+1) - winsum > k) {
            winsum -= nums[l];
            ++l;
        }

        /* Largest window is optimal due to max frequency of rightmost element. */
        res = max(res, r-l+1);
    }

    /* Return length of optimal window. */
    return res;
}
