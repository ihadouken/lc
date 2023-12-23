int findNthDigit(int n){
    int base, num, digits;
    base = 9;
    digits = 1;
    num = 0;

    while (n > (long) base * digits) {
        n -= (long) base * digits;
        num += base;
        base *= 10;
        ++digits;
    }

    num += n / digits;
    if (n % digits) {
        ++num;
        for (int i = 0; i < digits - (n % digits); ++i)
            num /= 10;
    }

    return num % 10;
}
