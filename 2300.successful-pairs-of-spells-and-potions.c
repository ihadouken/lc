/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int cmp(void *x, void *y) {
    return *((int*) x) - *((int*) y);
}

/* Approach: Sorting + Binary Search, Complexity: O(logn * (m+n)), O(1)
 * where m -> number of spells and n -> number of potions
 */
int* successfulPairs(int* spells, int spellsSize, int* potions, int potionsSize, long long success, int* returnSize){
    int i, l, r, m;

    /* Sort potions as the res[i] i.e. no. of potions is independant of order. */
    qsort(potions, potionsSize, sizeof(int), cmp);

    /* Iterate over the spells. */
    for (i = 0; i < spellsSize; ++i) {
        l = 0;
        r = potionsSize - 1;

        /* Find the potion of least strength which is successful for a spell. */
        while (l < r) {
            m = l + (r-l) / 2;

            if ((long long) potions[m] * spells[i] >= success)
                r = m;
            else
                l = m + 1;
        }

        /* All potions of higher strength will always be successful. The index
         * of an element is the number of elements preceeding it in the array.
         * Subtract the array size with it to find potions successful with spell
         * i.e. number of potions with strength >= minimum strength.
         */
        if ((long long) potions[l] * spells[i] >= success)
            spells[i] = potionsSize - l;
        else
            spells[i] = 0;
    }

    /* Return spells array as result for each spell overwrote its strength. */
    *returnSize = spellsSize;
    return spells;
}
