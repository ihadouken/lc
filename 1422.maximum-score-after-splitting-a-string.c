int max(int x, int y) {
    if (x > y)
        return x;
    return y;
}

/* Approach: Precomputation, Complexity: O(n), O(1) */
int maxScore(char* s) {
    /* "lsum" and "rsum" hold sum of zeroes and sum of ones in left and right
     * substrings respecitively. Maxscore holds the maximum score seen so far.
     */
    int len, lsum, rsum, maxscore;
    lsum = rsum = maxscore = 0;
    len = strlen(s);

    /* Precompute the total number of ones into "rsum" as the right substring has
     * all chars of the string in the beginning.
     */
    for (int i = 0; i < len; ++i) {
        if (s[i] == '1')
            ++rsum;
    }

    /* Iterate over the string and include every char into left substring one by
     * one while shrinking the right substring. "rsum" decrements if a 1 from the
     * right substring is added to left but "lsum" increments if a zero is added.
     */
    for (int i = 0; i < len - 1; ++i) {
        if (s[i] == '0')
            ++lsum;
        else
            --rsum;
        maxscore = max(maxscore, rsum+lsum);
    }

    /* Return the maximum score produced by any partitioning. */
    return maxscore;
}
