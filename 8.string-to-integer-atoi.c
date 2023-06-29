#define TRUE 1
#define FALSE 0

int isInt(char ch) {
    if (ch >= '0' && ch <= '9')
        return ch - '0';
    return -1;
}

int myAtoi(char * s){
    if (s == NULL)
        return 0;

    int i, negative, overmin, digit, num;
    /* special flag for handling INT_MIN */
    overmin = FALSE;
    i = 0;

    /* strip leading spaces */
    while (s[i] == ' ')
        i++;

    /* sign check */
    if (s[i] == '-') {
        negative = TRUE;
        i++;
    }
    else {
        if (s[i] == '+')
            i++;
        negative = FALSE;
    }

    num = 0;
    /* parse first number in string */
    while ((digit = isInt(s[i])) != -1) {
        if (num > INT_MAX / 10) {
            overmin = TRUE;
            num = INT_MAX;
            break;
        }
        else if (num == INT_MAX / 10) {
            if (digit == INT_MAX % 10) {
                num = INT_MAX;
                break;
            }
            if (digit > INT_MAX % 10) {
                overmin = TRUE;
                num = INT_MAX;
                break;
            }
        }
        num *= 10;
        num += s[i] - '0';
        i++;
    }

    /* adjust result if number was negative */
    if (negative) {
        if (overmin)
            return INT_MIN;
        num *= -1;
    }

    return num;
}
