int findMin(int* nums, int numsSize){
    int l, r, m;
    l = 0;
    r = numsSize - 1;

    while (l < r) {
        m = l + (r-l) / 2;
        if (nums[m] < nums[r])
            r = m;
        else if (nums[m] > nums[r])
            l = m + 1;
        else
            --r;
    }

    return nums[l];
}
