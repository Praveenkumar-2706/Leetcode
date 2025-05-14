class Solution {
    public int maxProfit(int[] prices) {
        int minprice = Integer.MAX_VALUE;
        int maxprofit = 0;
        if (prices.length <= 1) return 0;
        for(int price : prices){
            minprice = Math.min(price,minprice);
            maxprofit = Math.max(price-minprice,maxprofit);
        }
        return maxprofit;
    }
}