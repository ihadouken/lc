long long waysToBuyPensPencils(int total, int cost1, int cost2){
    int pencost;
    long long ways;
    pencost = ways = 0;

    /* Consider every scenario of buying pens i.e. 0 pens, 1 pen, 2 pens etc. */
    while (pencost <= total) {
        /* Try to find number of pencils that can be bought with the money left.
         * Also, account for the scenario when no pencils are bought. This gives
         * us the number of ways in which pencils can be bought with the remaining
         * money. Add the number of ways to the total number of ways.
         */
        ways += (total - pencost) / cost2 + 1;
        pencost += cost1;
    }

    /* Return the total number of ways pens and pencils can be bought. */
    return ways;
}
