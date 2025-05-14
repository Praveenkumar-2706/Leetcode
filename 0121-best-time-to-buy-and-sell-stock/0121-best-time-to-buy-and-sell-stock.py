class Solution(object):
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        minprice = float("inf");
        maxprofit = 0;
        for price in prices:
            minprice = min(minprice,price);
            maxprofit = max(maxprofit, price-minprice);
        return maxprofit