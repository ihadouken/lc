int max(int x, int y) {
    if (x > y)
        return x;
    return y;
}

/* Approach: Sliding Window, Complexity: O(n) */
int maxRotateFunction(int* nums, int numsSize){
    /* Maintain a left window and a right window. */
    int i, lsum, lpsum, rpsum, rsum, res;
    lsum = rsum = 0;
    lpsum = rpsum = 0;
    
    /* Initially, the right window contains all elements excluding the first one. */
    for (i = 1; i < numsSize; ++i)
        rsum += nums[i];

    /* Initially, the left window contains no elements. */
    for (i = 1; i < numsSize; ++i)
        rpsum += nums[i] * i;

    /* The output of the rotate function will equal the sum of products of elemnts
     * with their indices for both windows. The right window shrinks by one
     * element and left window expands by one element on each iteration.
     */
    res = lpsum + rpsum;

    for (i = 1; i < numsSize; ++i) {
        /* Decrementing product sum by window sum shifts the product weights
         * (indices) by one i.e. weights 1, 2, 3 becomes 0, 1, 2 for the same elements.
         * Then, remove the traversed element from the right window.
         */
        rpsum -= rsum;
        rsum -= nums[i];

        /* Add the previously traversed element to left window. Its product weight
         * is always the last index (n-1). Decrease the weights of all elements
         * in left window by one as a new element is inserted at the rear.
         */
        lpsum += nums[i-1] * (numsSize - 1);
        lpsum -= lsum;
        lsum += nums[i-1];

        /* Check if current product sum is the maximum. */
        res = max(res, lpsum+rpsum);
    }

    return res;
}
