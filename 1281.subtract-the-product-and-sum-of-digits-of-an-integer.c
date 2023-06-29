int subtractProductAndSum(int n){
    int sum, product, digit;
    sum = 0;
    product = 1;

    while(n > 0) {
        /* Get the rightmost digit. */
        digit = n % 10;

        /* Add and multiply the digit with sum and product respectively. */
        sum += digit;
        product *= digit;

        /* Shrink the number by one digit from the right. */
        n /= 10;
    }

    return product - sum;
}
