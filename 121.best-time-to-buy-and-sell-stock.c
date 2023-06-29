int maxProfit(int* prices, int pricesSize){
    int profit, max_profit, min_price, i;

    max_profit = 0;
    min_price = prices[0];
    /* Store the best profit while looking for a lower buying price and better profit out of it. */
    for (i = 1; i < pricesSize; ++i) {
        if (prices[i] < min_price)
            min_price = prices[i];
        else if (prices[i] - min_price > max_profit)
            max_profit = prices[i] - min_price;
    }
    return max_profit;
}
