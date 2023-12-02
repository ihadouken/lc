/* Approach: Greedy, Complexity: O(n), O(1) where n -> number of terms in the
 * fibonacci series <= k.
 */
int findMinFibonacciNumbers(int k){
    int n1, n2, new_n1, new_n2, count;
    count = 0;
    n1 = n2 = 1;

    /* Find the first element in the fibonacci series x such that x >= k. */
    while (n2 < k) {
        new_n2 = n1 + n2;
        n1 = n2;
        n2 = new_n2;
    }

    /* Starting from x upto the base numbers of the series, find elements <= k.
     * Since movement is from larger to smaller in the series, always the max
     * possible element (<= k) is considered for the sum. This leads to sum
     * comprising of minimum number of elements from the series. If the number
     * y was found, now find the highest element for k-y and so on until k
     * becomes 0 i.e. all elements summing up to k have been encountered.
     */
    while (k > 0) {
        if (n2 <= k) {
            ++count;
            k -= n2;
        }

        /* Computation of fibonacci elements in reverse. */
        new_n1 = n2 - n1;
        n2 = n1;
        n1 = new_n1;
    }
    /* Return the count of elements summing up to k. */
    return count;
}
