char nextGreatestLetter(char* letters, int lettersSize, char target){
    int l, r, m;
    l = 0;
    r = lettersSize - 1;

    while (l < r) {
        m = l + (r-l) / 2;
        if (letters[m] > target)
            r = m;
        else
            l = m + 1;
    }

    if (letters[l] > target)
        return letters[l];
    return letters[0];
}
