char * mergeAlternately(char * word1, char * word2){
    int i, s1, j, s2, k;
    s1 = strlen(word1);
    s2 = strlen(word2);

    char* merged = (char*) malloc((s1+s2+1)*sizeof(char));
    i = j = k = 0;

    while (i < s1 || j < s2) {
        if (i < s1)
            merged[k++] = word1[i++];
        if (j < s2)
            merged[k++] = word2[j++];
    }

    merged[k] = '\0';
    return merged;
}
