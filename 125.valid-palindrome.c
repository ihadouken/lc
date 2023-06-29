bool isAlpha(char ch) {
    if ((ch >= 'A' && ch <= 'Z') || (ch >= 'a' && ch <= 'z') || (ch >= '0' && ch <= '9'))
        return true;
    return false;
}

char toLower(char ch) {
    // lowercase version = uppercase letter + 32
    if (ch >= 'A' && ch <= 'Z')
        return ch + 32;
    return ch;
}

bool isPalindrome(char * s){
    int l, r;
    l = 0;
    r = strlen(s) - 1;

    while (l < r) {
        // ignore left if not an alphanumeric
        if (!isAlpha(s[l])) {
            l++;
            continue;
        }

        // ignore right if not an alphanumeric
        if (!isAlpha(s[r])) {
            r--;
            continue;
        }

        // check if letters are same irrespective of case
        if (toLower(s[l]) == toLower(s[r])) {
            l++;
            r--;
        }
        else
            return false;
    }

    return true;
}
