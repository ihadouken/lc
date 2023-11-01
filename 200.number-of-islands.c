void dfs(char** grid, int gridSize, int* gridColSize, int i, int j) {
    /* Return if out of bounds from the grid. */
    if (i < 0 || j < 0 || i >= gridSize || j >= gridColSize[i])
        return;
    /* Return if current square is not unvisited land. */
    if (grid[i][j] != 1)
        return;

    /* Mark the land square visited using a -ve siqn.  */
    grid[i][j] = -1;

    /* Visit all four neighbours of current land square to explore the entire island. */
    dfs(grid, gridSize, gridColSize, i-1, j);
    dfs(grid, gridSize, gridColSize, i+1, j);
    dfs(grid, gridSize, gridColSize, i, j-1);
    dfs(grid, gridSize, gridColSize, i, j+1);
}

/* Approach: DFS + Recursion + In-place operations, Complexity: O(m*n), O(m*n) */
/* Note: Each square is visited at most five times. All squares need to be stored
 *       in recursion stack if the entire grid is one big island. */

int numIslands(char** grid, int gridSize, int* gridColSize) {
    int i, j, islands;
    islands = 0;

    /* Convert chars. into ints for easier processing. */
    for (i = 0; i < gridSize; ++i)
        for (j = 0; j < gridColSize[i]; ++j)
            grid[i][j] -= '0';

    /* Iterate over all sqaures in the grid. */
    for (i = 0; i < gridSize; ++i) {
        for (j = 0; j < gridColSize[i]; ++j) {
            if (grid[i][j] == 1) {
                /* Univisited land means a new island is discovered. */
                ++islands;
                /* Explore the newly found island by DFS on found land square. */
                dfs(grid, gridSize, gridColSize, i, j);
            }
        }
    }

    /* Return count of islands. */
    return islands;
}
