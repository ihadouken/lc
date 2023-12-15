/* Tip: Increment by SPACE to convert A..Z -> a..z */
char* toLowerCase(char* s) {
    char* res;
    res = s;

    while (*s) {
        if ('A' <= *s && *s <= 'Z')
            *s = *s + ' ';
        ++s;
    }

    return res;
}
