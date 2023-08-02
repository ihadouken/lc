/* Approach: Sorting + Binary Search, Complexity: O(n), O(1) */

/* Comparator to sort the input in ascending order. */
int cmp(void *x, void *y) {
    return *((int*)x) - *((int*)y);
}

/* Find the last occurence of a target in a sorted input. */
int findLast(int *nums, int numsSize, int target) {
    int l, r, m, result;
    l = 0;
    r = numsSize - 1;

    while (l <= r) {
        m = l + (r-l) / 2;
        if (nums[m] <= target)
            l = m + 1;
        else
            r = m - 1;

        if (nums[m] == target)
            result = m;
    }
    return result;
}

/* Find the first occurence of a target in a sorted input. */
int findFirst(int *nums, int numsSize, int target) {
    int l, r, m, result;
    l = 0;
    r = numsSize - 1;
    result = -1;

    while (l <= r) {
        m = l + (r-l) / 2;
        if (nums[m] >= target)
            r = m - 1;
        else
            l = m + 1;

        if (nums[m] == target)
            result = m;
    }
    return result;
}

int countKDifference(int* nums, int numsSize, int k){
    int i, first, last, pairs;
    pairs = 0;

    qsort(nums, numsSize, sizeof(int), cmp);

    for (i = 0; i < numsSize-1; ++i) {
        /* Find the total number of occurences of x+k i.e. total number of y
         * such that mod(x-y) = k. Total number of occurences if given by the
         * length of the subarray [first, last]. Find first and last occurence
         * using binary search.
         */
        first = findFirst(&nums[i+1], numsSize-i-1, nums[i]+k);
        last = findLast(&nums[i+1], numsSize-i-1, nums[i]+k);

        /* Increment pairs by the occurence count (if any) of x+k for x. */
        if (first != -1)
            pairs += last - first + 1;
    }
    return pairs;
}
