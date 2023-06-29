int getRomanValue(char roman) {
    switch (roman) {
        case 'I':
            return 1;
        case 'V':
            return 5;
        case 'X':
            return 10;
        case 'L':
            return 50;
        case 'C':
            return 100;
        case 'D':
            return 500;
        case 'M':
            return 1000;
        default:
            return -1;
    }
}

int romanToInt(char * s){
    int i, num;
    num = i = 0;

    while (s[i+1] != '\0') {
        num += (getRomanValue(s[i]) < getRomanValue(s[i+1])) ? -getRomanValue(s[i]) : getRomanValue(s[i]);
        i++;
    }
    num += getRomanValue(s[i]);

    return num;
}
