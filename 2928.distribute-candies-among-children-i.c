int distributeCandies(int n, int limit) {
    int i, j, k, max, count;
    max = fmin(limit, n);
    count = 0;

    for (i = 0; i <= max; ++i) {
        for (j = 0; j <= max; ++j) {
            for (k = 0; k <= max; ++k) {
                if (i+j+k == n)
                    ++count;
            }
        }
    }

    return count;
}
