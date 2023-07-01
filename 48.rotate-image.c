void swap (int* x, int* y) {
    int temp;
    temp = *x;
    *x = *y;
    *y = temp;
}

void rev (int* arr, int arrSize) {
    int i, l, r;
    l = 0;
    r = arrSize - 1;

    while (l < r) {
        swap(&arr[l], &arr[r]);
        l++;
        r--;
    }
}

void rotate(int** matrix, int matrixSize, int* matrixColSize){
    int i, j;

    /* Generate the mirror of the matrix along the left (principal) diagonal. */
    for (i = 0; i < matrixSize - 1; i++) {
        for (j = i+1; j < matrixColSize[i]; j++) {
            swap(&matrix[i][j], &matrix[j][i]);
        }
    }

    /* Reverse all rows. */
    for (i = 0; i < matrixSize; i++)
        rev(matrix[i], matrixColSize[i]);
}
