class Solution(object):
    def maxProfit(self, prices):
        profit=0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i+1 , len(prices)):
                sell = prices[j]
                profit = max(profit , sell-buy)
        return profit