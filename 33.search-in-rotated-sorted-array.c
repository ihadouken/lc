int search(int* nums, int numsSize, int target){
    int l, r, m;
    l = 0;
    r = numsSize - 1;

    while (l <= r) {
        m = (l + r) / 2;
        if (nums[m] == target)
            return m;

        if (nums[m] < nums[l]) {
            if (target <= nums[r] && target > nums[m])
                l = m + 1;
            else
                r = m - 1;
        }
        else {
            if (target >= nums[l] && target < nums[m])
                r = m - 1;
            else
                l = m + 1;
        }
    }
    return -1;
}
