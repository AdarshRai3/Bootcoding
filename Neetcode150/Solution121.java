public class Solution121 {

    public int maxProfit(int[] prices) {
        // Frist we take the maxProfit variable and intialise with 0;
        int maxProfit = 0;
        // Second we need to intialise the minPrice to prices[0]
        int minPrices = prices[0];

        // Now we start iterating through the prices[0] to find out is there a price
        // which low than our intialise price if yes than we replace our current
        // minPrice with that prices[i]
        for (int i = 0; i < prices.length; i++) {
            minPrices = prices[i] < minPrices ? prices[i] : minPrices;
            // For caluclation of maxProfit we need to use simple price[i]-minPrice
            maxProfit = (prices[i] - minPrices) > maxProfit ? prices[i] - minPrices : maxProfit;
        }
        // end of the loop we will return the maxPrice
        return maxProfit;
    }

}
// -----------------------------------------------------
// Time Complexity : O(N);
// Space Complexity : O(1);
