/* Binary Exponentiation (recursive): O(logn), O(logn) */
// double binExp(double x, long n){
//     if (n == 0)
//         return 1;
//
//     if (n < 0) {
//         n = -1 * n;
//         x = 1/x;
//     }
//
//     if (n % 2)
//         return x * binExp(x*x, n/2);
//     return binExp(x*x, n/2);
// }

/* Binary Exponentiation (iterative): O(logn), O(1) */
double binExp(double x, long n){
    /* Trivial cases. */
    if (x == 0)
        return 0;
    if (n == 0 || x == 1)
        return 1;

    /* Evaluate exponent for reciprocal of x if n < 0. */
    if (n < 0) {
        /* Built-in abs() fails here as it only works with ints. */
        n = n * -1;
        x = 1/x;
    }

    double exp = 1;
    /* Until base case, can't divide further. */
    while (n) {
        /* If n is odd: Convert problem to divisible i.e. even.
         *              x^n -> x^(n-1) * x^1 -> x * x^(n-1) */
        /* This case always occurs at the last iteration i.e. n = 1, meaning the exponent
         * calculated into 'x' by the former iterations always ends up into the 'exp' variable. */
        if (n % 2) {
            exp *= x;
            n--;
        }

        /* If n is even: Divide problem to half i.e n/2.
         *               x^n -> x^(n/2 * 2) -> (x^2)^(n/2) -> (x*x)^(n/2) */
        else {
            x *= x;
            n /= 2;
        }
    }
    return exp;
}

double myPow(double x, int n){
    /*  long data type is required for n as it may equal INT_MIN.
     *  But, absolute of INT_MIN = INT_MAX + 1 which can't be stored as int. */
    return binExp(x, (long) n);
}
