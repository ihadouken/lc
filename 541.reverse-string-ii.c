/* Helper to reverse a substring given indices of both ends. */
void reverse_sub(char* s, int l, int r) {
    char temp;
    while (l < r) {
        temp = s[l];
        s[l] = s[r];
        s[r] = temp;

        ++l;
        --r;
    }
}

/* Approach: Two Pointer, Complexity: O(n), O(1) */
char * reverseStr(char * s, int k){
    int start, stop, size;
    size = strlen(s);
    /* Characters between start and stop (inclusive) = substring to reverse. */
    start = 0;
    stop = k-1;

    /* Keep reversing every k characters until there exists no substring of k
     * characters. 'start' will point an index higher than last index after the
     * last substring is reversed.
     */
    while (start < size - 1) {
        /* If the last substring doesn't contain enough (minimum k) characters,
         * still reverse the substring of fewer characters.
         */
        if (stop > size - 1)
            stop = size - 1;
        reverse_sub(s, start, stop);

        /* Skip the next k characters. Pointers actually point to a character
         * 2 * k characters after the previous value. */
        start += 2 * k;
        stop += 2 * k;
    }

    return s;
}
