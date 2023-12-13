/* Approach: Two Pointer, Complexity: O(n), O(1) */
char * removeStars(char * s){
    int r, w;
    r = w = 0;

    /* Read characters from the string left to right one-by-one. */
    while (s[r]) {
        /* If a star is encountered, move the write pointer backwards to the
         * previous character so that it can be overwritten. Otherwise, just
         * copy the read character to position pointed by write pointer.
         */
        if (s[r] == '*')
            --w;
        else {
            s[w] = s[r];
            ++w;
        }
        ++r;
    }

    /* Write pointer points to index where the next (not succeeded by star)
     * character is to be inserted. As all characters are exhausted, terminate
     * the string at this position now.
     */
    s[w] = '\0';
    return s;
}
