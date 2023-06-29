void duplicateZeros(int* arr, int arrSize) {
    int i, extras, r, w;

    /* find number of extra elements exceeding array space */
    for (i = extras = 0; i < arrSize; ++i) {
        if (arr[i] == 0)
            extras++;
    }

    /* find positions of read and write pointers */
    r = w = arrSize - 1;
    while (extras) {
        if (arr[r] == 0) {
            /* handle edge case when last zero's duplicate is first element to overflow the array */
            if (extras == 1) {
                arr[w--] = 0;
                extras--;
            }
            else
                extras -= 2;
        }
        else
            extras--;
        r--;
    }

    /* write transformed array with duplicate zeroes starting from the end */
    while(r >= 0) {
        arr[w--] = arr[r];
        if (arr[r] == 0)
            arr[w--] = 0;
        r--;
    }
}
