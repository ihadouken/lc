#define MAXCHAR 26

/* Approach: Counting, Complexity: O(m+n), O(26) */
/* Tip: Since both s and t are same length, to make every t an anagram of s,
 *      every undesired char in t must be deleted and an equal number of missing
 *      desired chars must be inserted.
 */
int minSteps(char * s, char * t){
    int i, steps;
    i = steps = 0;
    /* Initialize all char counts = 0. */
    int chcounts[MAXCHAR] = {0};

    /* Record all counts of desired chars (using s). */
    while (s[i]) {
        ++chcounts[s[i]-'a'];
        ++i;
    }

    /* Account for desired chars already in t by decrementing char counts of s. */
    i = 0;
    while (s[i]) {
        --chcounts[t[i]-'a'];
        ++i;
    }

    /* Sum counts of undesired chars and missing desired chars. */
    for (i = 0; i < MAXCHAR; ++i)
        steps += abs(chcounts[i]);

    /* An operation constitutes removing an undesired char and adding a missing desired char. */
    return steps/2;
}
