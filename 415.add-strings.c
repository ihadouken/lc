char * addStrings(char * num1, char * num2){
    int i, j, k, digitsum, sumSize, carry;
    i = strlen(num1);
    j = strlen(num2);

    /* Create resultant of size = max(num1, num2) + 1. */
    sumSize = ((i > j) ? i : j) + 1;
    char* sum = (char*)malloc((sumSize+1) * sizeof(char));

    /* Traverse numbers from the LSB. */
    i--;
    j--;

    /* Populate resultant from the LSB. */
    k = sumSize - 1;
    carry = 0;

    /* Simulate standard pen-on-paper addition method. */
    while (i >= 0 || j >= 0 || carry > 0) {
        digitsum = carry;

        if (i >= 0) {
            digitsum += num1[i] - '0';
            i--;
        }

        if (j >= 0) {
            digitsum += num2[j] - '0';
            j--;
        }

        sum[k] = '0' + digitsum % 10;
        k--;
        carry = digitsum / 10;
    }

    /* If there was a carry after adding the last columns. */
    if (k == -1) {
        sum[sumSize] = '\0';
        return sum;
    }

    /* If not then shift all characters to left by one place. */
    while (k < sumSize - 1) {
        sum[k] = sum[k+1];
        k++;
    }
    sum[sumSize-1] = '\0';
    return sum;
}
