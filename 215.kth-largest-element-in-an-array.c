void swap(int* x, int* y) {
    int temp;
    temp = *x;
    *x = *y;
    *y = temp;
}

int partition(int* arr, int beg, int end) {
    int i, j, pivot;
    pivot = end;

    for (i = j = beg; i < pivot; i++) {
        if (arr[i] > arr[pivot]) {
            swap(&arr[i], &arr[j]);
            j++;
        }
    }

    swap(&arr[j], &arr[pivot]);
    return j;
}

// Recursive: O(n) (average)
void quickselect(int *arr, int beg, int end, int k) {
    int pivot;
    pivot = partition(arr, beg, end);

    if (pivot < k)
        quickselect(arr, pivot + 1, end, k);
    else if (pivot > k)
        quickselect(arr, beg, pivot - 1, k);
    // if pivot = k, no recursive call is made and the recursion comes to end.
}

// Iterative: O(n) (average)
/* void quickselect(int *arr, int beg, int end, int k) {
    int pivot;
    while (beg != end) {
        pivot = partition(arr, beg, end);

        if (pivot < k)
            beg = pivot + 1;
        else if (pivot > k)
            end = pivot - 1;
        else
            break;
    }
} */

int findKthLargest(int* nums, int numsSize, int k){
    /* Adjust k so that it points to required index. (which is off by one) */
    k--;
    quickselect(nums, 0, numsSize-1, k);
    return nums[k];
}
