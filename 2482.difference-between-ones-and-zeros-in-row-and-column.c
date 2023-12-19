/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */

/* Macros for matrix order. */
#define M gridSize
#define N gridColSize[0]

/* Approach: Precomputation, Complexity: O(m*n), O(m+n) */
int** onesMinusZeros(int** grid, int gridSize, int* gridColSize, int* returnSize, int** returnColumnSizes) {
    /* Use arrays to store diff of each row and column. Init all differences as 0. */
    int i, j, *rowdiffs, *coldiffs;
    rowdiffs = (int*) calloc(M, sizeof(int));
    coldiffs = (int*) calloc(N, sizeof(int));

    /* Increment diff for every 1 in row/column and decrement it for every 0.
     * Update difference of ith row and jth column for every A(i, j). */
    for (i = 0; i < M; ++i) {
        for (j = 0; j < N; ++j) {
            if (grid[i][j]) {
                ++rowdiffs[i];
                ++coldiffs[j];
            }
            else {
                --rowdiffs[i];
                --coldiffs[j];
            }
        }
    }

    /* diff of element (i, j) = diffs of row (i) + diff of column (j) */
    for (i = 0; i < M; ++i)
        for (j = 0; j < N; ++j)
            grid[i][j] = rowdiffs[i] + coldiffs[j];

    /* Each element was replaced with its diff. Return updated input grid. */
    *returnSize = gridSize;
    *returnColumnSizes = gridColSize;
    return grid;
}
