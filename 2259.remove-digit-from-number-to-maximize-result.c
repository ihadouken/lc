/* Auxillary function to left shift a string once. */
void shift(char* s) {
    while (*s) {
        *s = *(s+1);
        ++s;
    }
}

/* Approach: Greedy + Inplace Operation, Complexity: O(n), O(1) */
/* Tip: Greedily scan for digit occurences from left to right. Deleting a digit
 *      (i) succeeded by a higher digit (i+1) will always result in a higher
 *      number than deleting a digit after i.
 */
char* removeDigit(char* number, char digit) {
    char *res, *prev_occ;
    /* Save reference of 1st char. for returning later. */
    res = number;

    /* Iterater over the string left to right. */
    while (*number) {
        if (*number == digit) {
            /* Save last occurence's address in case its the last one. */
            prev_occ = number;
            /* Check the digit's successor to maximise number after deletion. */
            if (*(number+1) > digit)
                break;
        }
        /* Move on to process next digit in number. */
        ++number;
    }

    /* Delete a digit by left shifting all digits after it once. */
    shift(prev_occ);
    /* Return modified string after the deletion. */
    return res;
}
