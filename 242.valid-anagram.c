#define CHARSET_SIZE 26

bool isAnagram(char * s, char * t){
    int i;
    int chcounts[CHARSET_SIZE] = { 0 };

    i = 0;
    while (s[i] != '\0') {
        chcounts[s[i]-'a'] += 1;
        i++;
    }

    i = 0;
    while (t[i] != '\0') {
        chcounts[t[i]-'a'] -= 1;
        i++;
    }

    for (i = 0; i < CHARSET_SIZE; ++i) {
        if (chcounts[i])
            return 0;
    }
    return 1;
}
