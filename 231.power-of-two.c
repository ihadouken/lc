#define FALSE 0
#define TRUE 1

bool isPowerOfTwo(int n){
    // O(logn)
    // if (n < 1)
    //     return FALSE;
    //
    // while (n > 1) {
    //     if (n % 2)
    //         return FALSE;
    //     n /= 2;
    // }
    // return TRUE;

    // O(1)
    if (n > 0 && !(n & n-1))
        return TRUE;
    return FALSE;
}
