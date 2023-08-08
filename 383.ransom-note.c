#define CHARSET_SIZE 26

/* Approach: Counting, Complexity: O(m+n), O(1) */
/* Tip: Store frequencies of all characters of ransomNote. Then decrement the
 * count by the frequency of that character in magazine. After all this, if a
 * character occurs more in ransomNote than in magazine, its final count will
 * be > 0 (ransomNote can't be created from magazine) else the char's final
 * count <= 0. If the latter condition is true for each lowercase character,
 * then ransomNote can be created from magazine.
 */
bool canConstruct(char * ransomNote, char * magazine){
	int i;
	int chcounts[CHARSET_SIZE] = {0};
	while (*ransomNote != '\0')
		++chcounts[*ransomNote++ - 'a'];

	while (*magazine != '\0')
		--chcounts[*magazine++ - 'a'];

	for (i = 0; i < CHARSET_SIZE; ++i)
		if (chcounts[i] > 0)
			return false;
	return true;
}
