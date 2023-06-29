int pivotIndex(int* nums, int numsSize){
    int rsum, lsum, i;
    lsum = rsum = 0;

    for (i = 0; i < numsSize; i++)
        rsum += nums[i];

    for (i = 0; i < numsSize; i++) {
        rsum -= nums[i];
        if (lsum == rsum)
            return i;
        lsum += nums[i];
    }
    return -1;
}
