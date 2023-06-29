int strStr(char * haystack, char * needle){
    int i, j;
    i = j = 0;
    while(haystack[i] != '\0' && needle[j] != '\0') {
        if (haystack[i] == needle[j]) {
            i++;
            j++;
        }
        else {
            i = i-j+1;
            j = 0;
        }
    }
    if (needle[j] == '\0')
        return i-j;
    return -1;
}
