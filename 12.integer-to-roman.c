int copyRoman(char* from, char* to, int at) {
    int i;
    i = 0;

    while (from[i] != '\0')
        to[at++] = from[i++];
    return at;
}

char * intToRoman(int num){
    /* Maximum characters a roman numeral can have is 15. */
    char roman[16];
    int i, j, multiplier, nextRoman;

    char* romans[] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
    int ints[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};

    i = 0;
    nextRoman = 0;

    while (num > 0) {
        /* Find the next roman digit to use i.e. a roman digit can only be
         * used if its weight is smaller than the number itself. */
        while (num < ints[nextRoman])
            nextRoman++;

        /* How many times to use the digit ? (1..3) */
        multiplier = num / ints[nextRoman];
        for (j = 0; j < multiplier; j++)
            i = copyRoman(romans[nextRoman], roman, i);

        /* Update the number. */
        num %= ints[nextRoman];
        nextRoman++;
    }

    roman[i] = '\0';
    return strdup(roman);
}
