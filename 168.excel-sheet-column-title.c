void rev(char* s) {
    int l, r, temp;
    l = 0;
    r = strlen(s) - 1;

    while (l < r) {
        temp = s[l];
        s[l] = s[r];
        s[r] = temp;

        l++;
        r--;
    }
}

char * convertToTitle(int columnNumber){
    int i;
    char title[8];

    i = 0;
    while (columnNumber > 0) {
        title[i++] = 'A' + (columnNumber - 1) % 26;
        columnNumber = (columnNumber - 1) / 26;
    }
    title[i] = '\0';

    rev(title);
    return strdup(title);
}
