/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

/* Approach: Bit Hacks, Complexity: O(n), O(1) */
/* Tip: Since the input contains elements <= 1000, it is possible to store two
 *      such elements (each occupying 10 bits) in the same integer.
 */
// int* buildArray(int* nums, int numsSize, int* returnSize){
//     int i, tenbits;
//     /* A mask of 10 bits is required to access first 10 bits of an integer. */
//     tenbits = (1 << 10) - 1;
//
//     /* For each index, store the desired element of the index in bits 11-20. */
//     for (i = 0; i < numsSize; ++i)
//         nums[i] |= (nums[nums[i]] & tenbits) << 10;
//
//     /* Both input and output are now stored in the same array. Input is stored
//      * in bits 1-10 and output in bits 11-20. Shift each index 10 bits right so
//      * that the output bits overwrite input bits.
//      */
//     for (i = 0; i < numsSize; ++i)
//         nums[i] >>= 10;
//
//     *returnSize = numsSize;
//     return nums;
// }

/* Approach: Math, Complexity: O(n), O(1) */
/* Tip: Store two numbers in the same integer of the form pq + r where r < q.
 *      p can be extracted via dividing by q. Since r < q, r/q = 0.
 *      r can be extracted via modding by q. Since pq is multiple of q, pq % q = 0.  */

int* buildArray(int* nums, int numsSize, int* returnSize){
    /* q = size of input array. For every index, p = final value i.e. nums[nums[i]]
     * and r = input value i.e. nums[i]
     * For every i, get the old value for nums[nums[i]] (i.e. r) and store it as
     * the new value for nums[i] (i.e. p). Preserve old value for nums[i] as r.
     */
    int i;
    for (i = 0; i < numsSize; ++i)
        nums[i] = nums[nums[i]] % numsSize * numsSize + nums[i] % numsSize;

    /* Build the output by overwriting pq + r values with p. */
    for (i = 0; i < numsSize; ++i)
        nums[i] /= numsSize;

    *returnSize = numsSize;
    return nums;
}
