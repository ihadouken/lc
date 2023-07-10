#define SPACE ' '

int lengthOfLastWord(char * s){
    int beg, end;
    end = strlen(s) - 1;

    /* Find last word's ending. */
    while (s[end] == SPACE)
        end--;

    /* Assume the end is beginning. */
    beg = end;

    /* Now, find its starting. */
    while (beg > 0 && s[beg-1] != SPACE)
        beg--;

    return end - beg + 1;
}
