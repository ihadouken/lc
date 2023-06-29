/* finds the largest palindromic substring in a given string */

#include <string.h>

int grow_pdrome(char *str, int ptr1, int ptr2);

char * longestPalindrome(char * s){
    int beg, end, len1, len2, len;
    beg = end = 0;

    for (int i = 0; i < strlen(s); ++i) {
        len1 = grow_pdrome(s, i, i);
        len2 = grow_pdrome(s, i, i+1);

        if (len1 > len2)
            len = len1;
        else
            len = len2;

        if (len > end - beg) {
            beg = i - (len - 1) / 2;
            end = i + len / 2;
        }
    }
    s[end+1] = '\0';
    return &s[beg];
}

int grow_pdrome(char *str, int ptr1, int ptr2) {
    while (ptr1 >= 0 && ptr2 < strlen(str) && (str[ptr1] == str[ptr2])) {
        ptr1--;
        ptr2++;
    }
    return ptr2 - ptr1 - 1;
}
