/* Auxillary function to compute the sum of squared digits for a number. */
int getSum(int x) {
    int sum, digit;
    sum = 0;

    while (x) {
        digit = x % 10;
        x /= 10;
        sum += digit * digit;
    }

    return sum;
}

/* Approach: Cycle Detection (Slow/Fast pointers) */

/* For any number, if its unhappy, we just end up cycling between a set of values
 * in an infinite loop. Thus, problem reduces to detection  of cycle in the numbers
 * being checked for happiness. The cycle is present for every unhappy number
 * because if there is no cycle, the number must always increase when the sum of
 * digit squares in taken. This does not hold when number of digits > 2.
 *
 * For ex: For 3 digit numbers, 999 has the highest sum of squares of digits i.e.
 * 243 which still doesn't add another digit to the number and hence the number
 * can be no longer than 999.
 */

bool isHappy(int n){
    /* Check if number is happy without any iterations needed. */
    if (getSum(n) == 1)
        return true;

    /* Basic cycle detection using slow/fast pointers for unhappy numbers. */
    int slow, fast;
    slow = getSum(n);
    fast = getSum(getSum(n));

    while (fast != slow) {
        /* If terminal (1) is reached, there is no cycle i.e. number is happy. */
        if (fast == 1)
            return true;
        slow = getSum(slow);
        fast = getSum(getSum(fast));
    }

    /* If a cycle is detected at any iteration, number can't be happy. */
    return false;
}
