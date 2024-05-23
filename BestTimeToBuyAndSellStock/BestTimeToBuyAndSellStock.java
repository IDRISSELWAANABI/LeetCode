class Solution {
    public int maxProfit(int[] prices) {
        if (prices == null){
            return 0;
        }
        int max_profit = 0 ;
        int min_price = prices[0];
        for (int i=1;i<prices.length;i++){
            max_profit = Math.max(max_profit, prices[i]-min_price);
            min_price = Math.min(min_price, prices[i]);
        }
        return max_profit;
        
    }
}
