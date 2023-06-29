int min(int x, int y) {
    if (x < y)
        return x;
    return y;
}

int maxArea(int* height, int heightSize){
    int l, r, water, max;
    l = 0;
    r = heightSize - 1;
    max = 0;

    while (l < r) {
        water = (r - l) * min(height[l], height[r]);
        if (water > max)
            max = water;

        if (height[l] <= height[r])
            ++l;
        else
            --r;
    }
    return max;
}
