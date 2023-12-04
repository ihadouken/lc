/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
/* Tip: Increment every element with its prefix sums. */
int* runningSum(int* nums, int numsSize, int* returnSize){
    int i;
    for (i = 1; i < numsSize; ++i)
        nums[i] += nums[i-1];

    *returnSize = numsSize;
    return nums;
}
