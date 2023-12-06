/* Approach: Simulation, Complexity: O(n) */
/* Tip: Find the element > k consecutive elements. If None is, return max. */
int getWinner(int* arr, int arrSize, int k){
    int i, streak, winner;
    winner = streak = 0;

    /* Start with first element as winner and simulate game for entire array. */
    for (i = 1; i < arrSize; ++i) {
        /* If a element > winner, it is the new winner. */
        if (arr[i] > arr[winner]) {
            winner = i;
            streak = 0;
        }

        /* Maintain a streak of victories of the current winner. */
        ++streak;

        /* Return a winner if a limit of consecutive victories has been reached. */
        if (streak == k)
            return arr[winner];
    }

    /* If no element reached the target streak, return the last winner. */
    return arr[winner];
}
