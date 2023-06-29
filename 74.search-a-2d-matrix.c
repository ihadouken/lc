bool searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target){
    int l, r, m, searchrow;
    l = 0;
    r = matrixSize - 1;

    while (l <= r) {
        m = l + (r - l) / 2;
        if (matrix[m][0] < target)
            l = m + 1;
        else if (matrix[m][0] > target)
            r = m - 1;
        else
            return true;
    }

    if (r == -1)
        return false;

    searchrow = r;
    l = 0;
    r = matrixColSize[searchrow] - 1;

    while (l <= r) {
        m = l + (r - l) / 2;
        if (matrix[searchrow][m] < target)
            l = m + 1;
        else if (matrix[searchrow][m] > target)
            r = m - 1;
        else
            return true;
    }
    return false;
}
