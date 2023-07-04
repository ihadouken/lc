// Approach: Binary Search, Complexity: O(nlogn)

// int countLowerEqual(int *arr, int arrSize, int num) {
//     int i, count;
//     for (count = i = 0; i < arrSize; i++) {
//         if (arr[i] <= num)
//             count++;
//     }
//     return count;
// }
//
// int findDuplicate(int* nums, int numsSize){
//     int l, r, m;
//     /* Search space: [1, n] (numsSize = n + 1) */
//     l = 1;
//     r = numsSize - 1;
//
//     /* Normally, in a list of unique numbers, a number has a count of numbers
//      * smaller than or equal = its value. For example: In [3, 1, 4, 2], 3 has a
//      * count of 3.
//      * The smallest number in nums with count (of numbers smaller than or
//      * equal to itself) higher than its own value has a duplicate. This is
//      * because it has one extra number equal to itself i.e. the duplicate. */
//     while (l < r) {
//         m = l + (r - l) / 2;
//         /* If count is higher than own value for one number then it will be higher
//          * all subsequent numbers in search space. Thus, duplicated number lies
//          * to this number's right or its this number itself. */
//         if (countLowerEqual(nums, numsSize, m) > m)
//             r = m;
//         /* If count is normal, then the duplicated number lies to its right.  */
//         else
//             l = m + 1;
//     }
//     return l;
// }

// Approach: Floyd's tortoise and hare algorithm (Slow-Fast pointers)
// Complexity: O(n)

int findDuplicate(int* nums, int numsSize){
    int hare, tortoise;
    /* two pointers start from the beginning */
    hare = tortoise = nums[0];
    hare = nums[nums[hare]];
    tortoise = nums[tortoise];

    /* until they meet */
    while (tortoise != hare) {
        /* but one moves faster than the other */
        hare = nums[nums[hare]];
        tortoise = nums[tortoise];
    }

    /* Intersection is guranteed as the faster one catches up to the slower one. */

    /* Loop entry from this point is equal to the distance from start to loop entry outside the loop. */
    /* So start one pointer from start and one from the intersection point at same speed. */
    hare = nums[0];

    /* And they will endeed meet at the loop entry i.e. duplicated element. */
    while (tortoise != hare) {
        tortoise = nums[tortoise];
        hare = nums[hare];
    }

    return tortoise;
}
