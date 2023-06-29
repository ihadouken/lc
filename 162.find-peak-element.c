int findPeakElement(int* nums, int numsSize){
    int l, m, r;
    l = 0;
    r = numsSize - 1;

    // while (l < r) {
    //     m = l + (r-l) / 2;
    //     if (nums[m] > nums[m+1])
    //         r = m;
    //     else
    //         l = m + 1;
    // }
    // return l;

    while (l+1 < r) {
        m = l + (r-l) / 2;
        if (nums[m] > nums[m+1])
            r = m;
        else
            l = m;
    }

    if (nums[r] > nums[l])
        return r;
    return l;
}
