int cmp(const void *x, const void *y) {
    /* Cast to int pointer and then de-reference into local variables. */
    int n1 = *(int*) x;
    int n2 = *(int*) y;
    return n1 - n2;
}

int maximumElementAfterDecrementingAndRearranging(int* arr, int arrSize){
    /* Sort array in non-decreasing order. */
    qsort(arr, arrSize, sizeof(int), cmp);

    arr[0] = 1;
    /* Local Optimality: Decrement every element to maximum value that meets condition 2. */
    for (int i = 1; i < arrSize; i++) {
        if (arr[i] > arr[i-1] + 1)
            arr[i] = arr[i-1] + 1;
    }

    /* Last value will be maximum possible in array after modification. */
    return arr[arrSize-1];
}
