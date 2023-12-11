int countOperations(int num1, int num2){
    int ops;
    ops = 0;

    /* Keep subtracting until one of them becomes zero. */
    while (num1 > 0 && num2 > 0) {
        /* Always divide smaller number from larger one. */
        if (num1 > num2)
            num1 -= num2;
        else if (num2 > num1)
            num2 -= num1;

        /* If both are same, one more operation is required to make one of them 0. */
        else
            return ops + 1;

        /* Count number of operations. */
        ++ops;
    }

    /* Return number of operations. */
    return ops;
}
