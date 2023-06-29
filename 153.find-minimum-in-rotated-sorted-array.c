int findMin(int* nums, int numsSize){
    int l, r, m;
    l = 0;
    r = numsSize - 1;

    while (l < r) {
        m = l + (r-l) / 2;

        /* If mid is <= last element then it is an unrotated elements. Also,
         * all elements higher than it cannot be minimum. So, only mid and
         * the elements preceeding it can be the possible minimae. */
        if (nums[m] <= nums[r])
            r = m;
        /* If mid > first element, then it is a rotated element. Minima is
         * always the unrotated element and thus lies to its right. */
        else
            l = m + 1;
    }
    return nums[l];
}
