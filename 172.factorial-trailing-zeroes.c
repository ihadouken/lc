/* Approach: Math (Factorization + Divisibility), Complexity: O(log5(n)), O(1)
 * Tip: Count occurences of five as factor of n!.
 *
 * Intuition: A trailing zero occurs when 10 is present as factor. Also, number
 *            of trailing zeroes = number of occurences of 10 as a factor. 10
 *            occurs naturally as a factor when there exists a pair of 2 and 5
 *            as factors as 2*5 = 10. As n increases from n = 1, 5 as a factor
 *            occurs less frequently than 2. So, number of occurences of 10 as a
 *            factor = number of occurences of 5 as a factor.
 *
 *            To solve for n < 25, consider n! = n * n-1 * n-2 * n-3 ... 2 * 1.
 *            Number of occurences of 5 as factor in the expression = number of
 *            multiples of 5 = n / 5.
 *
 *            However, 25, 125, 625 have 2, 3 and 4 factors as 5 respectively. To
 *            account for these extra fives as factors, use a dynamic divisor
 *            which starts from 5, then becomes 25 to account every for 2nd
 *            occurence of 5 as factor of same number, then 125 to account every
 *            3rd occurence of 5, then 625 and so on.
 *
 *            This process stops when divisor is too big to divide n.
 */

int trailingZeroes(int n) {
    int div, five_count;
    five_count = 0;
    div = 5;

    while (div <= n) {
        five_count += n / div;
        div *= 5;
    }

    return five_count;
}
