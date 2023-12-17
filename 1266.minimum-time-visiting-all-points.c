int max(int x, int y) {
    if (x > y)
        return x;
    return y;
}

/* Approach: Math (Chebyshev's distance), Complexity; O(n), O(1) */
int minTimeToVisitAllPoints(int** points, int pointsSize, int* pointsColSize) {
    /* Init time as 0. */
    int time, i, fromx, fromy, tox, toy;
    time = 0;

    /* Iterate over all points to create path between them. */
    for (i = 1; i < pointsSize; ++i) {
        /* Coordinates of current location. */
        fromx = points[i-1][0];
        fromy = points[i-1][1];

        /* Coordinates of destination. */
        tox = points[i][0];
        toy = points[i][1];

        /* Try to move maximum diagonally to move both ways by unit distance in
         * one move. Closer coordinate is satisfied completely while moving
         * diagonally trying to satisfy the farther coordinate. Satisfy the
         * farther coordinate by moving horizontally/vertically. Total moves are
         * moves made to satisfy the farther one i.e. max(dx, dy).
         */
        time += max(abs(tox-fromx), abs(toy-fromy));
    }

    /* Return total moves/time. */
    return time;
}
