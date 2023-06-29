#define TRUE 1
#define FALSE 0

int minSubArrayLen(int target, int* nums, int numsSize){
    int l, r, winval, winsize, minsize, found;
    minsize = numsSize;
    winsize = winval = 0;
    found = FALSE;

    for (r = l = 0; r < numsSize; ++r) {
        winval += nums[r];
        winsize++;
        while (winval >= target) {
            if (!found)
                found = TRUE;
            if (winsize < minsize)
                minsize = winsize;
            winval -= nums[l];
            winsize--;
            l++;
        }
    }

    if (found)
        return minsize;
    return 0;
}
