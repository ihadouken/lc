#define SPACE ' '

void copyToken(char* from, int beg, int end, char* to) {
	int i = strlen()

}

char * reverseWords(char * s){
	int len, forward, beg;
	len = strlen(s);

	for (forward = beg = len-1; forward >= 0; forward--) {
		if (s[forward] == SPACE) {
			if (beg == forward) {
				beg--;
			}
			else {
				copyToken(s, forward+1, beg);
				beg = forward;
			}
		}
	}
}
