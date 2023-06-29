void reverse(int *arr, int arrSize) {
    int l, r, temp;
    l = 0;
    r = arrSize - 1;
    while (l < r) {
        temp = arr[l];
        arr[l] = arr[r];
        arr[r] = temp;

        l++;
        r--;
    }
}

void rotate(int* nums, int numsSize, int k){
    k %= numsSize;
    reverse(nums, numsSize);
    /* reverse first k elements */
    reverse(nums, k);
    /* reverse next numsSize-k elements */
    reverse(&nums[k], numsSize-k);
}
