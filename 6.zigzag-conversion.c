char * convert(char * s, int numRows) {
    int slen, i, c, row;
    int alt;
    slen = strlen(s);
    char res[slen+1];
    c = 0;

    if (numRows == 1)
        return s;

    for (row = 0; row < numRows; ++row) {
        i = row;
        alt = 1;
        while (i < slen) {
            res[c] = s[i];
            ++c;
            if ((alt == 1) && (row < (numRows - 1)))
                i += 2 * (numRows - row - 1);
            else
                i += 2 * row;
            if ((row != 0) && (row != numRows - 1))
                alt *= -1;
        }
    }
    res[c] = '\0';
    strcpy(s, res);
    return s;
}
