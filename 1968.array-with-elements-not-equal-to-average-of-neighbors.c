/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

/* Compartor to sort in ascending order. */
int cmp(const void* x, const void* y) {
    return *((int*) x) - *((int*) y);
}

void swap(int* x, int* y) {
    int temp;
    temp = *x;
    *x = *y;
    *y = temp;
}

/* Approach: Sorting + Wave Sorting, Complexity: O(nlogn), O(1) */
int* rearrangeArray(int* nums, int numsSize, int* returnSize){
    /* Sort the array to find median and then partition it accordingly. */
    qsort(nums, numsSize, sizeof(int), cmp);
    int i, j;
    i = 0;
    j = numsSize / 2;

    /* Move all elements >= (right for even length) mid on the even indices of
     * nums They swap places with numbers already on those indices. This results
     * in a[i-1] > a[i] < a[i+1] for all i.
     */
    while (i < numsSize-1 && j < numsSize) {
        swap(&nums[i], &nums[j]);
        i += 2;
        j += 1;
    }

    /* Return nums after performing the in-place wave sorting. */
    *returnSize = numsSize;
    return nums;
}
