/* Auxillary function to find the sum of digits in a number. */
int sum_digits(int num) {
    int sum;
    sum = 0;

    while (num > 0) {
        sum += num % 10;
        num /= 10;
    }

    return sum;
}

/* Approach: Math, Complexity: O(n*log(INT_MAX)), O(1) */
/* Tip: Visit every element in nums and maintain a sum of elements along with a
 *      sum of digits in the array. Return the absolute difference of both sums.
 */
int differenceOfSum(int* nums, int numsSize){
    int i, sum, dsum;
    sum = dsum = 0;

    for (i = 0; i < numsSize; ++i) {
        sum += nums[i];
        dsum += sum_digits(nums[i]);
    }

    return abs(sum-dsum);
}
