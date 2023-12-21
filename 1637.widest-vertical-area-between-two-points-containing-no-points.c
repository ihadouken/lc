/* Comparator to compare x-coordinate of two points.
 * qsort() calls cmp with (void) pointers to the elements to be compared.
 */
int cmp(const void *x, const void *y) {
    /* Cast "void ptr -> array" to "int ptr -> array" for dereferencing it to an
     * array pointer. Compute difference between first element of both arrays to
     * compare them.
     */
    const int *first = *(const int **) x;
    const int *second = *(const int **) y;
    return first[0] - second[0];
}

int max(int x, int y) {
    if (x > y)
        return x;
    return y;
}

/* Approach: Sorting, Complexity: O(nlogn), O(1) */
int maxWidthOfVerticalArea(int** points, int pointsSize, int* pointsColSize) {
    /* Order by x-coordinate in increasing order so that all vertical areas can
     * be visited in sequential order.  */
    qsort(points, pointsSize, sizeof(points[0]), cmp);

    int maxwidth, i;
    maxwidth = -1;

    /* Find the max (horizontal) width between bounds of any two points in the
     * plane by traversing (horizontally) from left to right and return it.
     */
    for (i = 1; i < pointsSize; ++i)
        maxwidth = max(maxwidth, points[i][0] - points[i-1][0]);
    return maxwidth;
}
