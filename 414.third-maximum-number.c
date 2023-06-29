int thirdMax(int* nums, int numsSize){
    /* find min index for assigning all three pointers */
    int i, min, max1, max2, max3;
    for (i = min = 0; i < numsSize; ++i) {
        if (nums[i] < nums[min])
            min = i;
    }

    /* try to find max three using 3-pointers */
    max1 = max2 = max3 = min;
    for (i = 0; i < numsSize; ++i) {
        if ((nums[i] == nums[max1]) || (nums[i] == nums[max2]) || (nums[i] == nums[max3]))
            continue;
        if (nums[i] > nums[max1]) {
            max3 = max2;
            max2 = max1;
            max1 = i;
        }
        else if (nums[i] > nums[max2]) {
            max3 = max2;
            max2 = i;
        }
        else if (nums[i] > nums[max3]) {
            max3 = i;
        }
    }

    /* check if max3 is distinct */
    if ((nums[max1] == nums[max2]) || (nums[max2] == nums[max3]))
        return nums[max1];
    return nums[max3];
}
