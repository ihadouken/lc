int trap(int* height, int heightSize){
    int max_h, stored, temp, beg, i;
    max_h = temp = stored = beg = 0;
    for (i = 0; i < heightSize; ++i) {
        if (height[i] < max_h)
            temp += max_h - height[i];

        else {
            stored += temp;
            temp = 0;
            max_h = height[i];
            beg = i;
        }
    }

    if (i == heightSize && temp != 0) {
        temp = max_h = 0;

        for (i = heightSize - 1; i >= beg; --i) {
            if (height[i] < max_h)
                temp += max_h - height[i];
            else {
                stored += temp;
                temp = 0;
                max_h = height[i];
            }
        }
    }
    return stored;
}
