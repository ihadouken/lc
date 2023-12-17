/* Approach: Two Pointer, Complexity: O(min(m, n)), O(1)
 * where, m -> total chars in word1 and n -> total chars in word2. */
bool arrayStringsAreEqual(char** word1, int word1Size, char** word2, int word2Size) {
    int i, j;
    char *c1, *c2;

    /* Two integer pointers keep track of current part of word. */
    i = j = 0;
    /* Two char pointers keep track of current char of current part of word. */
    c1 = word1[i];
    c2 = word2[j];

    /* Compare chars until word parts run out for word1 or word2. */
    while (i < word1Size && j < word2Size) {
        /* If end of word part is reached, point char pointer to first char in
         * next part of the word. */
        if (!*c1)
            c1 = word1[i];
        if (!*c2)
            c2 = word2[j];

        /* If compared chars don't equal, words are different. */
        if (*c1 != *c2)
            return false;
        ++c1;
        ++c2;

        /* If end of word part is reached, consider next part of the word. */
        if (!*c1)
            i += 1;
        if (!*c2)
            j += 1;
    }

    /* Both words must run out of word parts at the same time to be equal. */
    return i == word1Size && j == word2Size;
}
