/* Approach: Greedy, Complexity: O(n), O(1). */
int maxProfit(int* prices, int pricesSize){
    int i, cur_profit, profit;
    profit = cur_profit = 0;

    /* Since we can buy and sell multiple times, consider multiple transactions
     * where profit is possible. The total profit is the cummulative of profit
     * made with each Buy/Sell. We will always the have stock bought even selling
     * the same day if price falls the next day from buying day. */
    for (i = 0; i < pricesSize-1; i++) {
        /* If price goes down tomorrow, sell the stock. Record the profit made
         * with the current transaction into the total profit. If we bought
         * today (cur_profit = 0) we will sell the stock today with zero profit. */
        if (prices[i] > prices[i+1]) {
            profit += cur_profit;
            cur_profit = 0;
        }
        /* If price stays or goes up, don't sell but add to your current profit. */
        else
            cur_profit += prices[i+1] - prices[i];
    }

    /* Always sell at last day and check for profit. */
    if (cur_profit)
        profit += cur_profit;
    return profit;
}
