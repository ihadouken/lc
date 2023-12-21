/* Approach: Math (Squares and factors), Complexity: O(logn) */
/* Note: For a small input range TC for sqrt() is O(1) */

/* Tip: A bulb is on after the entire process if it is toggled odd times i.e.
 *      it has an odd number of factors (including 1 and itself). Only perfect
 *      perfect squares have an odd number of factors since one of them i.e.
 *      the square root doesn't make a pair. No need to count perfect squares
 *      in 1..n because if m = [sqrt(n)], n >= mth perfect squares and there
 *      exist m perfect squares till n (inclusive).
 */
int bulbSwitch(int n){
    return sqrt(n);
}

/* Approach: Binary Search + Math, Complexity: O(logn) */
/* Note: Same intuition with sqrt calculation using self-implemented bsearch. */
// int bulbSwitch(int n){
//     int l, r, m;
//     long msquare;
//     l = 1;
//     r = n;
//
//     while (l <= r) {
//         m = l + (r-l) / 2;
//         msquare = (long) m * m;
//         if (msquare > n)
//             r = m - 1;
//         else if (msquare < n)
//             l = m + 1;
//         else
//             return m;
//     }
//
//     return r;
// }
