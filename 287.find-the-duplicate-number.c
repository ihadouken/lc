int countLowerEqual(int *arr, int arrSize, int num) {
    int i, count;
    for (count = i = 0; i < arrSize; i++) {
        if (arr[i] <= num)
            count++;
    }
    return count;
}

int findDuplicate(int* nums, int numsSize){
    int l, r, m;
    /* Search space: [1, n] (numsSize = n + 1) */
    l = 1;
    r = numsSize - 1;

    /* Normally, in a list of unique numbers, a number has a count of numbers
     * smaller than or equal = its value. For example: In [3, 1, 4, 2], 3 has a
     * count of 3.
     * The smallest number in nums with count (of numbers smaller than or
     * equal to itself) higher than its own value has a duplicate. This is
     * because it has one extra number equal to itself i.e. the duplicate. */
    while (l < r) {
        m = l + (r - l) / 2;
        /* If count is higher than own value for one number then it will be higher
         * all subsequent numbers in search space. Thus, duplicated number lies
         * to this number's right or its this number itself. */
        if (countLowerEqual(nums, numsSize, m) > m)
            r = m;
        /* If count is normal, then the duplicated number lies to its right.  */
        else
            l = m + 1;
    }
    return l;
}
