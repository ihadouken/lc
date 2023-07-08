void setZeroes(int** matrix, int matrixSize, int* matrixColSize){
    int i, j, iflag, jflag;
    iflag = 0;
    jflag = 0;

    /* Mark first row (for columns to set zero) and first column (for rows to set zero.) */
    for (i = 0; i < matrixSize; i++) {
        for (j = 0; j < matrixColSize[i]; j++) {
            if (!matrix[i][j]) {
                /* Set marker to set column as zero. */
                matrix[0][j] = 0;
                /* Set marker to set row as zero. */
                matrix[i][0] = 0;

                /* Set markers for first row and column. */
                if (!i)
                    iflag = 1;
                if (!j)
                    jflag = 1;
            }
        }
    }

    /* Postpone first column and row as it will mess up row markers. */
    /* Zero marked columns. */
    for (j = 1; j < matrixColSize[0]; j++) {
        if (!matrix[0][j]) {
            for (i = 0; i < matrixSize; i++)
                matrix[i][j] = 0;
        }
    }
    /* Zero marked rows. */
    for (i = 1; i < matrixSize; i++) {
        if (!matrix[i][0]) {
            for (j = 0; j < matrixColSize[i]; j++)
                matrix[i][j] = 0;
        }
    }

    /* Set first column to zero if it had marker. */
    if (jflag) {
        for (i = 0; i < matrixSize; i++)
            matrix[i][0] = 0;
    }
    /* Set first row to zero if it had marker. */
    if (iflag) {
        for (j = 0; j < matrixColSize[0]; j++)
            matrix[0][j] = 0;
    }
}
