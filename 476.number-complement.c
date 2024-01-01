/* Approach: Bit Hack, Complexity: O(logn) */
/* Tip: The sum of a number with its complement always equals the number with
 *      all bits set i.e. 111...111. So, calculate this number and then minus
 *      the input from it to get the input's complement. To calculate this bit
 *      mask number:
 *      Find the next power of two and then decrement one from it.
 *              OR
 *      Bit shift zero and set 1st bit for number of times equal to the entire
 *      bit width of the input. To iterate number of times equal to bit width,
 *      right shift the number till all set bit fall off and the number = 0.

 * Example: If I: 5 i.e. 101
 *      mask = 0 then 1 then 11 then finally 111
 *      num = 101 then 010 then 001 and then finally 000

 * Example: If I: 5 i.e. 101
 *      Next power of two = 1000 i.e. 8
 *      Sum of complement with num = 1000 - 1 = 111 i.e. 7
 *      Complement = 111 - 101 = 010 i.e 2
 */
int findComplement(int num){
    if (num == 0)
        return 1;

    int sum, numcopy;
    sum = 0;
    numcopy = num;

    while (numcopy > 0) {
        sum = (sum << 1) | 1;
        numcopy >>= 1;
    }

    /* Find the power of two higher than input requires a long integer type as
     * 1 bit higher than the data type of input i.e. int is required.
     */
    // while (sum <= num)
    //     sum <<= 1;
    // --sum;

    return sum - num;

    /* This works because complement of num inverts all the 32 bits of the num.
     * Using &, only the inverted bits fitting within the bit width of num are
     * considered.
     */
    // return ~num & sum;
}
