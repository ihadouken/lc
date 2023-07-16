/* Approach: Divide and Conquer, Complexity: O(n) in average case. */
/* Tip: An instance of majority is always at index n/2, if the array is sorted.
 * Case 1: If majority is the smallest element, it occupies indices 0 .. n/2
 *         (total (n/2)+1 instances).
 * Case 2: If majority is the largest element, it occupies indices n/2 .. n-1
 *         if n is odd and indices (n/2)-1 .. n-1 if n is even.
 * Case 3: If majority is inbetween largest and smallest, it always occupies
 *         some (n/2)+1 indices between the two ends of the array including
 *         the n/2 index.
 */

// void swap(int* x, int* y) {
//     int temp;
//     temp = *x;
//     *x = *y;
//     *y = temp;
// }
//
// int partition(int* nums, int beg, int end) {
//     int i, j;
//     for (i = j = beg; i < end; i++) {
//         if (nums[i] < nums[end]) {
//             swap(&nums[i], &nums[j]);
//             j++;
//         }
//     }
//     swap(&nums[end], &nums[j]);
//     return j;
// }
//
// // Recursive implementation.
// // void setMajority(int* nums, int numsSize, int beg, int end) {
// //     int pivot = partition(nums, beg, end);
// //
// //     /* Found correct element to put at some index to the left of numsSize/2,
// //      * go right to find numsSize/2. */
// //     if (pivot < numsSize/2)
// //         return setMajority(nums, numsSize, pivot+1, end);
// //
// //     /* Found correct element to put at some index to the right of numsSize/2,
// //      * go left to find numsSize/2. */
// //     else if (pivot > numsSize/2)
// //         return setMajority(nums, numsSize, beg, pivot-1);
// //
// //     /* Implicit return when pivot = numsSize/2 */
// // }
//
// // Iterative implementation.
// void setMajority(int* nums, int numsSize, int beg, int end) {
//     int pivot;
//     while (beg < end) {
//         pivot = partition(nums, beg, end);
//         if (pivot < numsSize/2)
//             beg = pivot + 1;
//         else if (pivot > numsSize/2)
//             end = pivot - 1;
//         else
//             break;
//     }
// }
//
// int majorityElement(int* nums, int numsSize){
//     /* Find the element (i.e. majority) placed at index numsSize/2 in a sorted version of nums.
//      * Also put this element at numsSize/2. */
//     setMajority(nums, numsSize, 0, numsSize-1);
//
//     /* This element will always be majority. */
//     return nums[numsSize/2];
// }

/* Approach: Boyer-Moore Algorithm, Complexity: O(n) in all cases */
/* Principle: Majority has 1 more occurence then the rest of elements combined.
 * Assume an element to be majority. If same element is encountered, we increase
 * its count. If some other element is found, we decrement it. If the count of
 * the majority reaches zero, it means that the rest of elements have instances
 * equal in number than the majority. The assumption is wrong. Assume the element
 * at this position to be majority and the count is set to one. The others will
 * be able to cancel out n/2 instances of the majority but even then one instance
 * higher than n/2 will let the algorithm find the majority.
 */
int majorityElement(int* nums, int numsSize){
    int i, majority, count;
    majority = nums[0];
    count = 0;
    for (i = 0; i < numsSize; ++i) {
        if (nums[i] == majority)
            ++count;
        else
            --count;

        if (!count) {
            majority = nums[i];
            count = 1;
        }
    }
    return majority;
}
