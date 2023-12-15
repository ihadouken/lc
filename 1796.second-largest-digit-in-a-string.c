/* Approach: Two Pointer, Complexity: O(n), O(1) */
/* Tip: Maintain maximum and 2nd maximum during traversal. */

int secondHighest(char* s) {
    char max1, max2;
    max1 = max2 = '\0';

    while (*s) {
        /* Ignore chars equal to max1 or max2 to avoid max1 = max2 situation. */
        if ('0' <= *s && *s <= '9' && *s != max1 && *s != max2) {
            if (*s > max1) {
                max2 = max1;
                max1 = *s;
            }
            else if (*s > max2) {
                max2 = *s;
            }
        }
        ++s;
    }

    /* Ensure that max2 was set to distinct 2nd maximum. */
    if (max2 && max1 != max2)
        return max2 - '0';
    return -1;
}
