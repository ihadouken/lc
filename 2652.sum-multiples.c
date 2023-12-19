/* Find the sum of first k multiples of a number (inclusive). */
int sum_k_multiples(int num, int k) {
    /* First k multiples of a number p form an A.P. -> p, 2p, 3p ... k terms.
     * Sum of A.P. with a = d = p and n = k -> n/2 * [2a + (n-1)d].
     */
    return ((2*num + (k-1)*num) * k) / 2;
}

/* Approach: Math(Principle of Inclusion/Exclusion), Complexity: O(1) */
/* Tip: n(AUBUC) = n(A) + n(B) + n(C) - n(A∩B) - n(B∩C) - n(A∩C) + n(A∩B∩C) as
 *      stated in set theory. For our problem,
 *        A -> Element divisible by 3
 *        B -> Element divisible by 5
 *        C -> Element divisible by 7
 *        A∩B -> Element divisible by both 3 and 5 i.e. by 15.
 *        B∩C -> Element divisible by both 5 and 7 i.e. by 35.
 *        A∩C -> Element divisible by both 3 and 7 i.e. by 21.
 *        A∩B∩C -> Element divisible by 3, 5 and 7 i.e. by 105.
 */
int sumOfMultiples(int n){
    int sum;

    sum += sum_k_multiples(3, n/3) + sum_k_multiples(5, n/5) + sum_k_multiples(7, n/7);
    sum -= sum_k_multiples(15, n/15) + sum_k_multiples(35, n/35) + sum_k_multiples(21, n/21);
    sum += sum_k_multiples(105, n/105);

    return sum;
}
