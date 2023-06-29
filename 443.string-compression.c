int compress(char* chars, int charsSize){
    int i, j, grp, glen, power;
    i = j = 0;
    while (i < charsSize) {
        glen = 0;
        grp = chars[i];

        while ((i < charsSize) && (chars[i] == grp)) {
            ++i;
            ++glen;
        }

        chars[j] = grp;
        j++;

        if (glen > 1) {
            power = (int) pow(10, (int) log10(glen));
            while (power > 0) {
                chars[j] = '0' + (glen / power % 10);
                ++j;
                power /= 10;
            }
        }
    }
    return j;
}
