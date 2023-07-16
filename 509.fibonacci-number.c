/* Approach: Recursion (Top-Bottom), Complexity: O(2^n), O(n) (call stack) */
// int fib(int n){
//     if (n == 0 || n == 1)
//         return n;
//     return fib(n-1) + fib(n-2);
// }

/* Approach: Recursion + Dynamic Programming, Complexity: O(n), O(n) (memoization) */
// int myfib(int n, int* memo){
//     /* Base Cases. */
//     if (n == 0 || n == 1)
//         return n;
//
//     /* If the value for F(n) was memoized, we don't need to recurse. */
//     if (memo[n] != 0)
//         return memo[n];
//
//     /* Calculate the value for F(n) and then fill the memo entry for it. */
//     int res = myfib(n-1, memo) + myfib(n-2, memo);
//     memo[n] = res;
//     return res;
// }
//
// int fib(int n) {
//     /* Allocate an array for memoization in the heap. Here, dp[n] will have the
//      * memo for F(n) so the size is n+1. The indices 0 and 1 will remain unused.
//      */
//     int* dp = (int*) calloc(n+1, sizeof(int));
//     int fibval = myfib(n, dp);
//     free(dp);
//     return fibval;
// }

/* Approach: Iterative (Bottom-Up), Complexity: O(n), O(1) */
int fib(int n) {
    if (n == 0 || n == 1)
        return n;

    int i, num1, num2, sum;
    num1 = 0;
    num2 = 1;

    /* Compute F(2)..F(n) (inclusive) */
    for (i = 2; i <= n; ++i) {
        sum = num1 + num2;
        num1 = num2;
        num2 = sum;
    }

    return num2;
}

