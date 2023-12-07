int max(int x, int y) {
    if (x > y)
        return x;
    return y;
}

/* Tip: Return the maximum row sum from the matrix. */
int maximumWealth(int** accounts, int accountsSize, int* accountsColSize){
    int i, j, max_wealth, wealth;
    max_wealth = 0;

    for (i = 0; i < accountsSize; ++i) {
        wealth = 0;

        for (j = 0; j < accountsColSize[i]; ++j)
            wealth += accounts[i][j];

        max_wealth = max(max_wealth, wealth);
    }

    return max_wealth;
}
