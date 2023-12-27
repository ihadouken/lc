/* Approach: Binary Search, Complexity: O(logn), O(1) */
int arrangeCoins(int n){
    int beg, end, mid;
    long reqd;
    /* Number of rows can't be < 0. Can't make more rows than there are coins. */
    beg = 0;
    end = n;

    /* Find number of rows via binary search. */
    while (beg <= end) {
        mid = beg + (end - beg) / 2;
        /* Find the coins required to create assumed (mid) rows. */
        reqd = ((long) (1 + mid) * mid) / 2;

        /* Coins required > available, assume a lower number of rows. */
        if (reqd > n)
            end = mid - 1;
        /* Coins required < available, assume a higher number of rows. */
        else if (reqd < n)
            beg = mid + 1;
        /* Exact coins available for creating assumed rows. */
        else
            return mid;
    }

    /* Return the max number of rows requiring coins < available coins. */
    return end;
}
