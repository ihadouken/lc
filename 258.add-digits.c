// Tip: Don't do unnecessary work.

// Approach: The digital sums repeat themselves after every 9 numbers.
// After adding each digit, keep the sum in range of a digit by modding with 9.

// O(log(num))
// int addDigits(int num){
//     int res, digit;
//     res = 0;
//
//     while (num > 0) {
//         digit = num % 10;
//         num /= 10;
//         res += digit;
//         res = 1 + (res - 1) % 9;
//     }
//     return res;
// }

// Approach: If digital sums repeat after every 9 numbers, we can directly mod the num.
// The mod has to be offset by 1 to the left as 9 % 9 = 0 but the digital root is 9.

// O(1)
int addDigits(int num){
    if (!num)
        return 0;
    return 1 + (num - 1) % 9;
}
