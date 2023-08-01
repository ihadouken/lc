double max(double x, double y) {
    if (x > y)
        return x;
    return y;
}

/* Approach: Sliding Window + Math (Incremental Mean), Complexity: O(n), O(1) */
/* Tip: Instead of finding the mean of all subarrays of length k (brute force),
 *      use a subarray window and maintain the window's mean.

 *      - New mean after adding an element to the window,
 *          (Mean * Number of elements + increment) / (Number of elements + 1)
 *      - New mean after removing an element from the window,
 *          (Mean * Number of elements - decrement) / (Number of elements - 1)
 *      - New mean after removing an element from the window while adding
 *        another simultaneously,
 *          (Mean * Number of elements + increment - decrement) / Number of elements
 */

double findMaxAverage(int* nums, int numsSize, int k){
    int l, r, winsize;
    double mean, max_mean;
    l = r = 0;
    winsize = 0;
    mean = 0;
    /* Corner case: Input has one element equal to INT_MIN. */
    max_mean = INT_MIN;

    for (r = 0; r < numsSize; ++r) {
        /* Too few elements. Add this element to the mean. */
        if (winsize < k) {
            mean = mean * winsize + nums[r];
            ++winsize;
            mean = mean / winsize;
        }
        /* Subarray capacity full. Remove a previous element and add this element
         * to the mean i.e. look for a better window. */
        else {
            max_mean = max(max_mean, mean);
            mean = (mean * winsize + nums[r] - nums[l]) / winsize;
            ++l;
        }
    }

    /* Corner case: Best window = last k elements of the input. */
    return max(max_mean, mean);
}
