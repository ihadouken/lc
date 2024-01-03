/* Approach: Binary Search, Complexity: O(logn) */
/* Tip: When two items at a time are added to a list, it remains even in length.
 *      But, when a single item is added to it, the length becomes odd.

 * Extra Tip: In an array, the number of elements to the left of an index always
 *            equals the index itself.

 * When we are at the first occurence of a twin,
 * Case 1: If we are at an odd index, it means there are odd number of elements
 *         to the left, thus the single element is to our left. The rear end of
 *         the search space is set to just before the mid.
 * Case 2: If the index is even, the number of elements to the left are even.
 *         Thus the single element can only exist to our right. The front end
 *         of the search space is set to mid (otherwise the current element
 *         will also end up with one instance).

 * When we are at the second occurence of a twin or the single number itself,
 * Case 3: If we are at an odd index, we have odd elements to the left. Thus,
 *         the single element is to the left or this is the single element.
 *         Set the end of the search space to mid.
 * Case 4: If index is even, we need to search right. Set the search space's
 *         start to just after mid.
 */
int singleNonDuplicate(int* nums, int numsSize){
    int l, r, m;
    l = 0;
    r = numsSize - 1;

    while (l < r) {
        m = l + ((r - l) >> 1);
        if (nums[m] == nums[m+1]) {
            if (m % 2)
                r = m - 1;
            else
                l = m;
        }
        else {
            if (m % 2)
                l = m + 1;
            else
                r = m;
        }
    }
    return nums[l];
}
