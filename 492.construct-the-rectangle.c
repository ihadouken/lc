/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

/* Appraoch: Two Pointer, Complexity: O(Area) */
// int* constructRectangle(int area, int* returnSize){
//     *returnSize = 2;
//     int* res = (int*) malloc(sizeof(int) * 2);
//
//     /* Set length -> maximum dimension, breadth -> minimum dimension */
//     int l, b;
//     l = res[0] = area;
//     b = res[1] = 1;
//     
//     /* Breadth can't be higher than length.*/
//     while (l >= b) {
//         /* Area too low ? Increase breadth. */
//         if (l * b < area)
//             ++b;
//         /* Area too high ? Decrease length. */
//         else if (l * b > area)
//             --l;
//         /* Correct area. */
//         else {
//             /* If more optimal dimensions are found, remember them instead. */
//             if (l - b < res[0] - res[1]) {
//                 res[0] = l;
//                 res[1] = b;
//             }
//
//             /* Another valid area can't be found with this length or breadth. So,
//              * advance both pointers. */
//             ++b;
//             --l;
//         }
//     }
//
//     /* Return the most optimal rectangle dimensions. */
//     return res;
// }

/* Find square root of area using binary search. */
int bsqrt(int x) {
    int l, r, m;
    long msquared;
    l = 1;
    r = x;

    while (l <= r) {
        m = l + (r - l) / 2;
        msquared = (long) m * m;

        if (msquared < x)
            l = m + 1;
        else if (msquared > x)
            r = m - 1;
        else
            return m;
    }

    return r;
}

/* Approach: Math + Binary Search, Complexity: O(logn + sqrt(n)), O(1) */
int* constructRectangle(int area, int* returnSize){
    *returnSize = 2;
    int* res = (int*) malloc(sizeof(int) * 2);
    
    /* As l * b = area and l >= b, b can't exceed square root of area. */
    int b;
    b = bsqrt(area);

    /* Find max b such that l * b = area. 1 <= b <= sqrt(area). */
    while (b > 0) {
        /* l needs to be an integer. */
        if (area % b == 0) {
            res[0] = area / b;
            res[1] = b;
            return res;
        }

        /* Try a lower b if current b doesn't meet criteria. */
        --b;
    }

    /* This code will never be reached but is here to please the compiler. */
    res[0] = area;
    res[1] = 1;
    return res;
}
