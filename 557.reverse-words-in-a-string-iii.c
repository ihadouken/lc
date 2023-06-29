#define SPACE ' '
#define END '\0'

void revslice(char* s, int stop) {
    int i, j, temp;
    i = 0;
    j = stop - 1;
    while (i < j) {
        temp = s[i];
        s[i] = s[j];
        s[j] = temp;

        i++;
        j--;
    }
}

char * reverseWords(char * s){
    /* beg: keeps track of current word start 
     * forward: gets next word token */
    int beg, forward;
    beg = forward = 0;

    while (s[beg] != END) {
        /* reverse newly found word token */
        if (s[forward] == SPACE || s[forward] == END) {
            revslice(&s[beg], forward-beg);
            /* point to starting of next word */
            if (s[forward] != END)
                forward++;
            beg = forward;
        }
        /* keep going */
        else
            forward++;
    }
    return s;
}
