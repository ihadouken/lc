int cmp(void* x, void* y) {
    return *((int*) x) - *((int*) y);
}

/* Approach: Sorting + Two Pointers, Complexity: O(nlogn), O(1) */
int findPairs(int* nums, int numsSize, int k){
    qsort(nums, numsSize, sizeof(int), cmp);

    int l, r, diff, count;
    count = 0;
    /* Use two pointers one after the other. */
    l = 0;
    r = 1;

    while (r < numsSize) {
        diff = nums[r] - nums[l];
        /* Difference too low. Moving right makes the pointers farther and
         * increases difference.
         */
        if (l == r || diff < k)
            ++r;

        /* Difference too high. Moving left makes the pointers closer and
         * decreases difference.
         */
        else if (diff > k)
            ++l;

        /* Suitable pair found. Move both pointers to search for new pairs.
         * Move r to point to a different value to ensure next pair is unique.
         */
        else {
            ++count;
            ++l;
            ++r;
            while (r < numsSize && nums[r] == nums[r-1])
                ++r;
        }
    }
    return count;
}
