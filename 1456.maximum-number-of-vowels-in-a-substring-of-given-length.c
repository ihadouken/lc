/* Check if a character is a vowel. */
bool isVowel(char ch) {
    if (ch == 'a' || ch == 'i' || ch == 'e' || ch == 'o' || ch == 'u')
        return true;
    return false;
}

/* Select maximum out of two integers. */
int max(int x, int y) {
    if (x > y)
        return x;
    return y;
}

/* Approach: Sliding Window, Complexity: O(n), O(1) */
int maxVowels(char * s, int k){
    int len, r, l, vcount, res;
    len = strlen(s);
    res = vcount = l = 0;

    /* Add characters to the right of window one at a time. */
    for (r = 0; r < len; ++r) {
        /* Increment counter if newly added character is a vowel. */
        if (isVowel(s[r]))
            ++vcount;

        /* Pop off the character at the left when window exceeds limit i.e. k.
         * Decrement counter if popped character was a vowel.
         */
        if (r-l+1 > k) {
            if (isVowel(s[l]))
                --vcount;
            ++l;
        }

        /* Window with maximum vowel count is most optimal. */
        res = max(res, vcount);
    }

    /* Return the optimal (maximum) vowel count. */
    return res;
}
