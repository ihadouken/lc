int removeElement(int* nums, int numsSize, int val){
    int i, j;
    i = 0;
    for (j = 0; j < numsSize; j++) {
        if (nums[j] != val) {
            nums[i] = nums[j];
            i++;
        }
    }
    return i;
}
