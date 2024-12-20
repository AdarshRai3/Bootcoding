public class StockBuySell {
    public int maxProfit(int[] prices) {
        int max = 0 ;
        int min = prices[0];
        for(int i = 0;i<prices.length;i++){
           min=prices[i]<min?prices[i]:min; // find and set min value
           int target = (prices[i]-min); // set value target to set max 
           max=target>max?target:max; // if target is greater than max , then set max as target
        }
       return max;
   }
}
