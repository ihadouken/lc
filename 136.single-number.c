/* Approach: Bit Hack, Complexity: O(n), O(1) */
int singleNumber(int* nums, int numsSize){
    int i, setbits;

    /* Maintain the decimal form of seen set (1) bits. */
    setbits = nums[0];

    /* Visit a number and XOR it with the 'setbits'. XOR is used to unset set
     * bits common between 'setbits' and nums[i]. This way the duplicate of
     * a number nullifies its previous occurence's set bits in 'setbits'.
     */
    for (i = 1; i < numsSize; ++i)
        setbits ^= nums[i];

    /* At the end, setbits equals the single number as it had no duplicate
     * which could cancel its set bits.
     */
    return setbits;
}
