class Solution {
    public void duplicateZeros(int[] arr) {
        /* find last element to copy in result */
        int r, w, len;
        for (r = len = 0; len < arr.length; r++) {
            if (arr[r] == 0)
                len += 2;
            else
                len++;
        }
        --r;

        /* handle edge case where a zero's duplicate is the first element to be thrown off */
        w = arr.length-1;
        if (len == arr.length + 1) {
            arr[w] = 0;
            w--;
            r--;
        }

        /* write the output with doubled zeroes into the array */
        while (r >= 0) {
            arr[w] = arr[r];
            w--;
            if (arr[r] == 0) {
                arr[w] = 0;
                w--;
            }
            r--;
        }
    }
}
