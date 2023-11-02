/* Auxillary function to compute max. */
int max(int x, int y) {
    if (x > y)
        return x;
    return y;
}

int dfs(int** grid, int gridSize, int* gridColSize, int i, int j) {
    /* Stop exploring when outside grid's bounds.  */
    if (i < 0 || j < 0 || i >= gridSize || j >= gridColSize[i])
        return 0;

    /* Stop exploring if a water or visited land block is encountered. */
    if (grid[i][j] != 1)
        return 0;

    /* Mark land block as visited by negative marking. */
    grid[i][j] = -1;

    /* Explore the neighbouring blocks of the just visited block and add up their
     * areas to area of island computed till the current block.
     */
    return dfs(grid, gridSize, gridColSize, i+1, j) + dfs(grid, gridSize, gridColSize, i-1, j) + dfs(grid, gridSize, gridColSize, i, j+1) + dfs(grid, gridSize, gridColSize, i, j-1) + 1;
}

/* Approach: DFS + Recursion + Negative Marking, Complexity: O(m*n), O(m*n) */
int maxAreaOfIsland(int** grid, int gridSize, int* gridColSize) {
    int i, j, maxarea;
    maxarea = 0;

    for (i = 0; i < gridSize; ++i) {
        for (j = 0; j < gridColSize[i]; ++j) {
            /* Unvisited block of land -> unexplored island. */
            if (grid[i][j] == 1)
                /* Maintain the maximum area seen. */
                maxarea = max(maxarea, dfs(grid, gridSize, gridColSize, i, j));
        }
    }

    /* Return the maximum area. */
    return maxarea;
}
