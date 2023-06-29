int calcTime(int* piles, int pilesSize, int speed) {
    int i, time;
    for (time = i = 0; i < pilesSize; ++i)
        time += piles[i] / speed + (piles[i] % speed != 0);
    return time;
}

int max(int* nums, int numsSize) {
    int i, max;
    for (max = i = 0; i < numsSize; ++i) {
        if (nums[i] > nums[max])
            max = i;
    }

    return nums[max];
}

int minEatingSpeed(int* piles, int pilesSize, int h){
    int l, r, k, time;
    l = 1;
    r = max(piles, pilesSize);

    while (l < r) {
        k = l + (r - l) / 2;
        time = calcTime(piles, pilesSize, k);

        if (time > h)
            l = k + 1;
        else
            r = k;
    }
    return l;
}
