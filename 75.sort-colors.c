// #define COLS 3

/* Apprach: Counting Sort, Complexity: O(n), O(3) ~ O(1) */
// void sortColors(int* nums, int numsSize){
//     int i, j;
//     int counts[COLS] = {0};
//
//     /* Count occurences of each color (0, 1 and 2). Each index has count of
//      * of instances of the index in nums. */
//     for (i = 0; i < numsSize; ++i)
//         ++counts[nums[i]];
//
//     /* Overwrite nums by putting the correct number of each type i as stored
//      * at counts [i]. */
//     j = 0;
//     for (i = 0; i < COLS; ++i) {
//         while (counts[i]) {
//             nums[j++] = i;
//             --counts[i];
//         }
//     }
// }

/* Approach: Two pointers, Complexity: O(1) */
void swap(int* x, int* y);
void sortColors(int* nums, int numsSize){
    int i, j;
    /* Move all zeroes to the left of the array.
     * After this, indices 0 .. j-1 will have zeroes and indices j+1 .. n-1
     * will have ones or twos. */
    for (i = j = 0; i < numsSize; ++i) {
        if (nums[i] == 0) {
            swap(&nums[i], &nums[j]);
            ++j;
        }
    }

    /* Move all ones to the right of zeroes but the left of twos.
     * Let j0 be the position of the last zero. After this, indices j0+1 .. j-1
     * will contain ones and indices j+1 .. n-1 will have twos. */
    for (i = j; i < numsSize; ++i) {
        if (nums[i] == 1) {
            swap(&nums[i], &nums[j]);
            ++j;
        }
    }
}

void swap(int* x, int* y) {
    int temp;
    temp = *x;
    *x = *y;
    *y = temp;
}
