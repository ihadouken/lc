#define VOWELS 10

/* Get index of given vowel in "counts". */
int getIndex(char vowel) {
    switch (vowel) {
        case 'A':
            return 0;
        case 'E':
            return 1;
        case 'I':
            return 2;
        case 'O':
            return 3;
        case 'U':
            return 4;
        case 'a':
            return 5;
        case 'e':
            return 6;
        case 'i':
            return 7;
        case 'o':
            return 8;
        case 'u':
            return 9;
        default:
            return -1;
    }
}

/* Find vowel associated with given index in "counts". */
char getVowel(int index) {
    switch (index) {
        case 0:
            return 'A';
        case 1:
            return 'E';
        case 2:
            return 'I';
        case 3:
            return 'O';
        case 4:
            return 'U';
        case 5:
            return 'a';
        case 6:
            return 'e';
        case 7:
            return 'i';
        case 8:
            return 'o';
        case 9:
            return 'u';
        default:
            return '\0';
    }
}

/* Approach: Counting Sort, Complexity: O(n), O(1) */
char * sortVowels(char * s){
    int i, j, size;
    size = strlen(s);
    /* Initialize the count of every vowel to 0. */
    int counts[VOWELS] = {0};

    /* Record the count of each vowel in the input. */
    for (i = 0; i < size; ++i)
        if (getIndex(s[i]) != -1)
            ++counts[getIndex(s[i])];

    /* Replace every vowel with smallest vowel whose instances are not used up.
     * No need to check for j < VOWELS as there can't be a vowel replacement
     * until a vowel is encountered in the input string.
     */
    i = j = 0;
    for (i = j = 0; i < size; ++i) {
        if (getIndex(s[i]) == -1)
            continue;

        /* For every vowel, find the smallest vowel whose instances are not exhausted. */
        while (!counts[j])
            ++j;

        /* Decrement the vowel's count as one of its instances has been used. */
        s[i] = getVowel(j);
        --counts[j];
    }

    return s;
}
