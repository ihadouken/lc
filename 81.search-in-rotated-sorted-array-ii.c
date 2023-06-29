bool search(int* nums, int numsSize, int target){
    int l, r, m;
    l = 0;
    r = numsSize - 1;

    while (l <= r) {
        m = (l + r) / 2;
        if (nums[m] == target)
            return true;

        if (nums[m] > nums[r]) {
            if (target > nums[r] && target < nums[m])
                r = m - 1;
            else
                l = m + 1;
        }

        else if (nums[m] < nums[r]) {
            if (target <= nums[r] && target > nums[m])
                l = m + 1;
            else
                r = m - 1;
        }

        else {
            r--;
        }
    }
    return false;
}
