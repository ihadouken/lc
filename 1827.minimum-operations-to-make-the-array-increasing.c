/* Approach: Greedy, Complexity: O(n), O(1) */
int minOperations(int* nums, int numsSize){
    int op, i;
    op = 0;

    /* Ensure that every element is strictly higher than its predecessor. */
    for (i = 1; i < numsSize; ++i) {
        /* For two numbers A and B such that A <= B, to make A > B, A must be
         * incremented B - A + 1 times minimum so that A = B + 1.
         * Each increment is counted separately as per question. 
         */
        if (nums[i] <= nums[i-1]) {
            op += nums[i-1] + 1 - nums[i];
            nums[i] = nums[i-1] + 1;
        }
    }

    /* Return the tatal number of increments done on the array. */
    return op;
}
