/* Approach: Two Pointer, Complexity: O(n), O(1) */
bool isLongPressedName(char * name, char * typed){
    int i, j;
    i = j = 0;

    /* Process every typed character. */
    while (typed[j] != '\0') {
        /* If the last matched char was typed multiple times, "typed" is still
         * valid. Otherwise it contains some foreign char and is invalid. Also,
         * if the all chars in "name" are exhausted, check if only last char
         * occurs in the remaining portion of "typed".
         */
        if (name[i] == '\0' || name[i] != typed[j]) {
            if (j == 0 || typed[j] != typed[j-1])
                return false;
        }
        /* If a char matching with "name" is found, try to find its next char. */
        else
            ++i;
        ++j;
    }

    /* If all characters of "name" were typed, only then return true. */
    return name[i] == '\0';
}
