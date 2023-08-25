/* Approach: Math, Complexity: O(n), O(1) */

/* Tip: To find the total number of zero-filled subarrays, find the grand sum of
 *      number of subarrays of each zero-filled subarray with non-zero elements
 *      next to both its ends. This is because a subarray of zero-filled subarray
 *      is also a zero-filled subarray.
 */
long long zeroFilledSubarray(int* nums, int numsSize){
    long long res;
    int i, zero_beg, subsize;
    i = res = 0;

    /* Iterate over the array to consider all possible subarray startings. */
    while (i < numsSize) {
        /* A zero element is the first element of a zero-filled subarray. */
        if (nums[i] == 0) {
            zero_beg = i;
            /* Find the index of the last zero in zero-filled subarray. */
            while (i < numsSize - 1 && nums[i+1] == 0)
                ++i;

            /* Find the length of the zero-filled subarray. */
            subsize = i - zero_beg + 1;

            /* Find the number of subarrays of the zero-filled subarray. Number
             * of subarrays of array of size n = sum(1 .. n) = ((1+n) * n) / 2.
             */
            res += ((long) (1 + subsize) * subsize) / 2;
        }
        ++i;
    }

    return res;
}
