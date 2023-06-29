/* absolute value of integer */
int abs(int x) {
    if (x < 0)
        return -1 * x;
    return x;
}

/* comparator for sort in ascending order */
int cmp(const void *x, const void *y) {
    int n1, n2;
    n1 = *(int*)x;
    n2 = *(int*)y;

    if (n1 < n2)
        return -1;
    else if (n1 > n2)
        return 1;
    return 0;
}

int findMaxK(int* nums, int numsSize) {
    int left, right;

    /* sort the input first so all -ve numbers precede +ve numbers */
    qsort(nums, numsSize, sizeof(int), cmp);

    /* two-pointer to find the highest pair of +ve and -ve with equal magnitude. */ 
    left = 0;
    right = numsSize - 1;
    while (left < right && nums[left] < 0 && nums[right] > 0) {
        if (abs(nums[left]) > abs(nums[right]))
            left++;
        else if (abs(nums[left]) < abs(nums[right]))
            right--;
        else
            return abs(nums[left]);
    }

    return -1;
}
