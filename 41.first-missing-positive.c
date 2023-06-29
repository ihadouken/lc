/* Approach: Use array's positive elements to access the array. For example,
 * the element 3 will access 3rd position. A position is not accessed if the
 * coressponding natural number doesn't exist in the array. We find the first
 * such position in the array i.e first missing positive. */

int abs(int x) {
    if (x < 0)
        return x * -1;
    return x;
}

int firstMissingPositive(int* nums, int numsSize){
    int i;
    /* Make sure array only contains whole numbers. */
    for (i = 0; i < numsSize; ++i) {
        if (nums[i] < 0)
            nums[i] = 0;
    }

    /* Use array's elements as its indices and access it. */
    for (i = 0; i < numsSize; ++i) {
        /* check if the element can act as index */
        if (abs(nums[i]) > 0 && abs(nums[i]) <= numsSize) {
            /* mark accessed elements by negating them */
            if (nums[abs(nums[i])-1] > 0)
                nums[abs(nums[i])-1] *= -1;
            /* set zeroes to value that can't be used as index */
            else if (nums[abs(nums[i])-1] == 0)
                nums[abs(nums[i])-1] = -(numsSize + 1);
        }
    }

    /* Find the lowest index that wasn't accessed. */
    for (i = 0; i < numsSize; ++i) {
        if (nums[i] >= 0)
            return i+1;
    }

    /* If all possible positives were present. */
    return numsSize + 1;
}
