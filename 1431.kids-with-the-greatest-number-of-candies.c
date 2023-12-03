/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

/* Tip: For a child to have the most candies, their candies must be >= max candies
 *      before extra candy distrubution.
 */
bool* kidsWithCandies(int* candies, int candiesSize, int extraCandies, int* returnSize){
    int i, max;
    bool* res;

    res = (bool*) malloc(sizeof(bool)*candiesSize);
    max = INT_MIN;

    for (i = 0; i < candiesSize; ++i) {
        if (candies[i] > max)
            max = candies[i];
    }

    for (i = 0; i < candiesSize; ++i) {
        if (candies[i] + extraCandies >= max)
            res[i] = true;
        else
            res[i] = false;
    }

    *returnSize = candiesSize;
    return res;
}
