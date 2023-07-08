/* Approach: Search by eliminating a row/column, Complexity: O(m+n) */
/* Tip: Point at the top-right of the submatrix that can possibly have the target.
 * This submatrix will ultmately reduce to a single element in the worst case (with m+n eliminations). */

bool searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target){
    int i, j;
    /* Start from the top-right corner. */
    i = 0;
    j = matrixColSize[0] - 1;

    /* Loop until we point to an invalid element. */
    while (i < matrixSize && j >= 0) {
        /* Larger target can't exist in current row. */
        if (matrix[i][j] < target)
            i++;
        /* Smaller target can't exist in current column. */
        else if (matrix[i][j] > target)
            j--;
        else
            return true;
    }
    return false;
}
