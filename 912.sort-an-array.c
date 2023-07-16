/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
void merge(int* nums, int beg, int end) {
    int i, j, k, n, mid;
    mid = beg + (end - beg) / 2;
    i = beg;
    j = mid + 1;
    k = 0;
    n = end - beg + 1;

    /* Auxillary space for merging two sorted arrays. */
    int* merged = (int*) malloc(n * sizeof(int));

    /* Process until one of the arrays is completely traversed. Locally decide
     * from the two elements under consideration which should go next in merged.
     */
    while (i <= mid && j <= end) {
        if (nums[i] < nums[j])
            merged[k++] = nums[i++];
        else
            merged[k++] = nums[j++];
    }

    /* When only one array is left to process copy all its elements into merged.
     * Only one of the following two while loops will execute.
     */
    while (i <= mid)
        merged[k++] = nums[i++];
    while (j <= end)
        merged[k++] = nums[j++];

    /* Copy elements of the merged into their corresponding positions in nums. */
    for (k = 0; k < n; ++k)
        nums[beg+k] = merged[k];
}

void mergeSort(int* nums, int beg, int end) {
    /* Conquer: Only one element left i.e. array is trivially sorted. */
    if (beg >= end)
        return;

    /* Divide: Divide into two smaller halves. */
    int mid = beg + (end - beg) / 2;
    mergeSort(nums, beg, mid);
    mergeSort(nums, mid+1, end);

    /* Combine: Merge the sorted halves. */
    merge(nums, beg, end);
}

int* sortArray(int* nums, int numsSize, int* returnSize){
    mergeSort(nums, 0, numsSize-1);
    /* output size = input size */
    *returnSize = numsSize;
    /* Sorted array overwrote the original array. */
    return nums;
}
