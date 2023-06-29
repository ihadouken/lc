int removeDuplicates(int* nums, int numsSize){
    int i, j;
    i = 0;
    for (j = 1; j < numsSize; j++) {
        if (nums[j] != nums[j-1]) {
            i++;
            nums[i] = nums[j];
        }
    }
    return i+1;
}
