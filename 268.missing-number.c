int cmp(void* x, void* y) {
    return *((int*) x) - *((int*) y);
}

/* Approach: Sorting + Linear Scan, Complexity: O(nlogn), O(1) */
// int missingNumber(int* nums, int numsSize){
//     int i;
//     qsort(nums, numsSize, sizeof(int), cmp);
//
//     for (i = 0; i < numsSize; ++i) {
//         if (nums[i] != i)
//             return i;
//     }
//
//     return i;
// }

/* Approach: Sorting + Binary Search, Complexity: O(nlogn), O(1) */
/* Tip: Sort the array and return the min i such that i != nums[i]. */
// int missingNumber(int* nums, int numsSize){
//     qsort(nums, numsSize, sizeof(int), cmp);
//
//     if (nums[numsSize-1] == numsSize - 1)
//         return numsSize;
//
//     int l, r, m;
//     l = 0;
//     r = numsSize - 1;
//
//     while (l < r) {
//         m = l + (r-l) / 2;
//         if (m == nums[m])
//             l = m + 1;
//         else
//             r = m;
//     }
//
//     return l;
// }

/* Approach: Negative Marking, Complexity: O(n), O(1) */
/* Tip: Use the elements in the array to access the array. Thus, elements 1..n
 *      map to indices 0..n-1 Each element can access only one array index. Mark
 *      an accessed index by negating the element at that index. Return the index
 *      which wasn't accessed i.e. the one accessible by the missing number.
 */
// int missingNumber(int* nums, int numsSize){
//     /* Shift input range from 0..n to 1..n+1. for marking zeroes. */
//     int i, index;
//     for (i = 0; i < numsSize; ++i)
//         ++nums[i];
//
//     for (i = 0; i < numsSize; ++i) {
//         index = abs(nums[i]) - 1;
//         if (index < numsSize)
//             nums[index] *= -1;
//     }
//
//     for (i = 0; i < numsSize; ++i) {
//         if (nums[i] > 0)
//             break;
//     }
//
//     return i;
// }

/* Approach: Math, Complexity: O(n), O(1) */
/* Tip: The missing number will not be in the sum of array elements. But, it will
 *      be in the sum of first n natural numbers (or first n+1 whole numbers).
 *      Just subtract the sum of array from sum(0..n) to get the missing number.
 */
int missingNumber(int* nums, int numsSize){
    int i, reqd_sum, sum;
    sum = 0;

    /* Sum of arithmetic progression, Sn = ((a+l) * n) / 2 */
    reqd_sum = ((1 + numsSize) * numsSize) / 2;

    for (i = 0; i < numsSize; ++i)
        sum += nums[i];

    return reqd_sum - sum;
}
