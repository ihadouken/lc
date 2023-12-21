bool isVowel(char ch) {
    if (ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U' ||
        ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' )
        return true;
    return false;
}

void swap(char* x, char* y) {
    char temp;
    temp = *x;
    *x = *y;
    *y = temp;
}

/* Approach: Two Pointer, Complexity: O(n), O(1) */
char * reverseVowels(char * s){
    int l, r;
    l = 0;
    r = strlen(s) - 1;

    while (l < r) {
        /* Ignore consonants. */
        if (!isVowel(s[l]))
            ++l;
        else if (!isVowel(s[r]))
            --r;
        /* Swap pairs of vowels to only reverse the vowels in the string. */
        else {
            swap(&s[l], &s[r]);
            ++l;
            --r;
        }
    }

    return s;
}
