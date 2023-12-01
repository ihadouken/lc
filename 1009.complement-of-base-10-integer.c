int bitwiseComplement(int n){
    if (n == 0)
        return 1;

    int sum;
    sum = 1;

    while (sum <= n)
        sum <<= 1;
    --sum;

    return sum - n;
}
