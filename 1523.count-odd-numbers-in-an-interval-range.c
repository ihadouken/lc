/* Approach: Math (A.P.), Complexity: O(1) */
/* Tip: Modify low and high to be first and last odd numbers in the interval.
 *
 *      For an arithmetic progression, l = a + (n-1) * d
 *      Rewriting, we get, n = (l-a) / d + 1
 *
 *      where a = low (first term), d = 2 (common diff. for series of odds),
 *            l = high (last term), n = number of terms (unknown)
 *
 *      The only unknown i.e. n, can be easily found out.
 */

int countOdds(int low, int high){
    if (!(low%2))
        low++;
    if (!(high%2))
        high--;
    return (high-low) / 2 + 1;
}
