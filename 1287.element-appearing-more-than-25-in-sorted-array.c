/* Binary Search to find index of leftmost occurence of target in [l, r] */
int findLeftMost(int* arr, int l, int r, int target) {
    int m, ans;

    while (l <= r) {
        m = l + (r-l) / 2;
        if (arr[m] == target) {
            ans = m;
            r = m - 1;
        }
        else
            l = m + 1;
    }

    return ans;
}

/* Binary Search to find index of rightmost occurence of target in [l, r] */
int findRightMost(int* arr, int l, int r, int target) {
    int m, ans;

    while (l <= r) {
        m = l + (r-l) / 2;
        if (arr[m] == target) {
            ans = m;
            l = m + 1;
        }
        else
            r = m - 1;
    }

    return ans;
}

/* Approach: Binary Search, Complexity: O(logn), O(1) */
int findSpecialInteger(int* arr, int arrSize) {
    int c1, c2, c3, left, right;
    /* Since the desired element occupies > 25% of the array, there has to be at
     * one instance of it at index one-third / half / three-fourth of array. As
     * the array is sorted, all occurences occur together.
     */
    c1 = arrSize/4;
    c2 = arrSize/2;
    c3 = (3*arrSize) / 4;

    /* If an element spans two of the candidate positions, it is the answer. */
    if (arr[c1] == arr[c2])
        return arr[c1];
    if (arr[c2] == arr[c3])
        return arr[c2];

    /* Find the leftmost and rightmost occurence of elements at each of these
     * indices. Using this data, the number of occurences of element can be found.
     * The candidate occuring more than 1/4 times of the total number of elements
     * is the result.
     */
    /* Leftmost occurence of c1 occurs between index 0 to c1. */
    left = findLeftMost(arr, 0, c1, arr[c1]);
    /* Rightmost occurence of c1 occurs between index c1 to arrSize-1. */
    right = findRightMost(arr, c1, arrSize-1, arr[c1]);
    /* Find no. of occurences of the candidate using leftmost and rightmost index. */
    if (right - left + 1 > arrSize/4)
        return arr[c1];

    left = findLeftMost(arr, 0, c2, arr[c2]);
    right = findRightMost(arr, c2, arrSize-1, arr[c2]);
    if (right - left + 1 > arrSize/4)
        return arr[c2];

    left = findLeftMost(arr, 0, c3, arr[c3]);
    right = findRightMost(arr, c3, arrSize-1, arr[c3]);
    if (right - left + 1 > arrSize/4)
        return arr[c3];

    /* This line required for the compiler to not complain about no return value. */
    return -1;
}
