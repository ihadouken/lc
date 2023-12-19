int cmp(void *x, void *y) {
    return *((int*) x) - *((int*) y);
}

int countPairs(int* nums, int numsSize, int target){
    int l, r, pairs;
    qsort(nums, numsSize, sizeof(int), cmp);

    l = 0;
    r = numsSize - 1;
    pairs = 0;

    while (l < r) {
        if (nums[l] + nums[r] >= target)
            --r;
        else {
            pairs += r - l;
            ++l;
        }
    }

    return pairs;
}
