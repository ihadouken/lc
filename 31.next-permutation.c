void swap(int* x, int* y) {
    int temp;
    temp = *x;
    *x = *y;
    *y = temp;
}

void rev(int* nums, int beg, int end) {
    while (beg < end)
        swap(&nums[beg++], &nums[end--]);
}

void nextPermutation(int* nums, int numsSize){
    int k, i;
    k = numsSize - 2;
    while (k >= 0 && nums[k+1] <= nums[k])
        --k;

    if (k == -1) {
        rev(nums, 0, numsSize-1);
        return;
    }

    i = numsSize - 1;
    while (i > k && nums[i] <= nums[k])
        --i;

    swap(&nums[k], &nums[i]);
    rev(nums, k+1, numsSize-1);
}
