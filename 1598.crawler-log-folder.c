#define PREV "../"
#define CUR "./"

/* Approach: Stack (Emulation), Complexity: O(n), O(1) */
int minOperations(char ** logs, int logsSize){
    /* Instead of maintaining a stack, just maintain its length. */
    int i, depth;
    depth = 0;

    /* Iterate over all directory operations. */
    for (i = 0; i < logsSize; ++i) {
        /* When moving to previous directory, stack shrinks by one due to pop. */
        if (depth > 0 && strcmp(logs[i], PREV) == 0)
            --depth;

        /* When moving to a subdirectory, stack grows by one due to a push. */
        else if (strcmp(logs[i], PREV) != 0 && strcmp(logs[i], CUR) != 0)
            ++depth;
    }

    /* Return the depth of current position in filesystem i.e. stack size. */
    return depth;
}
