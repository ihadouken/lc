// bool canPlaceFlowers(int* flowerbed, int flowerbedSize, int n){
//     if (flowerbedSize == 1)
//         return !(flowerbed[0] && n);
//
//     int i;
//     i = 0;
//
//     while (i < flowerbedSize) {
//         if (!flowerbed[i]) {
//             if ((i == 0 && !flowerbed[i+1]) || (i == flowerbedSize - 1 && !flowerbed[i-1]) || (i > 0 && i < flowerbedSize - 1 && !flowerbed[i-1] && !flowerbed[i+1])) {
//                 n--;
//                 i += 2;
//             }
//             else
//                 i++;
//         }
//         else
//             i += 2;
//     }
//
//     return n <= 0;
// }

bool canPlaceFlowers(int* flowerbed, int flowerbedSize, int n){
    int i;
    for (i = 0; i < flowerbedSize; i++) {
        /* Check adjacent flowerbed only if it exists. */
        if (!flowerbed[i] && (i == 0 || !flowerbed[i-1]) && (i == flowerbedSize - 1 || !flowerbed[i+1])) {
            flowerbed[i] = 1;
            n--;
        }
    }

    /* Check if all flowers placed. */
    return n <= 0;
}

