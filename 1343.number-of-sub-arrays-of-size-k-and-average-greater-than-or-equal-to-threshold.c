/* Approach: Sliding Window + Math (Running Mean), Complexity: O(n), O(1) */
int numOfSubarrays(int* arr, int arrSize, int k, int threshold){
    int l, r, runsum, count;
    l = runsum = count = 0;

    for (r = 0; r < k; ++r)
        runsum += arr[r];
    if (runsum / k >= threshold)
        count += 1;

    for (r = k; r < arrSize; ++r) {
        runsum = runsum - arr[l] + arr[r];
        ++l;

        if (runsum / k >= threshold)
            count += 1;
    }
    return count;
}
