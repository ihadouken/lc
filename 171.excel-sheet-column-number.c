int titleToNumber(char * columnTitle){
    int i, num, chval;
    num = i = 0;

    while (columnTitle[i] != '\0') {
        chval = columnTitle[i++] - 'A' + 1;
        num = num * 26 + chval;
    }
    return num;
}
