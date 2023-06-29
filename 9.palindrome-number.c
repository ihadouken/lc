bool isPalindrome(int x){
    if (x < 0)
        return false;

    int digit, rev, tempx;
    rev = 0;
    tempx = x;
    while (tempx > 0) {
        if (rev > INT_MAX/10 || ((rev == INT_MAX/10) && (rev >= INT_MAX % 10)))
            return false;
        digit = tempx % 10;
        tempx /= 10;
        rev = rev * 10 + digit;
    }

    if (rev == x)
        return true;
    return false;
}
