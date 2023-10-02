int cmp(int* x, int* y) {
    return *((int*) x) - *((int*) y);
}

/* Aporoach: Sorting, Complexity: O(nlogn), O(1) */
/* Tip: APs always occur as sorted sequences with common term difference. */
bool canMakeArithmeticProgression(int* arr, int arrSize){
    int i, cdiff;
    qsort(arr, arrSize, sizeof(int), cmp);

    cdiff = arr[1] - arr[0];
    for (i = 0; i < arrSize - 1; ++i) {
        if (arr[i+1] - arr[i] != cdiff)
            return false;
    }

    return true;
}
