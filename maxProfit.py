class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        max_profit = 0
        buy = False
        prices.append(0)
        for i in xrange(1,len(prices)):
            if prices[i-1] < prices[i] and buy == False:
                buy_price = prices[i-1]
                buy = True
            elif prices[i-1] > prices[i] and buy == True:
                sell_price = prices[i-1]
                max_profit += sell_price - buy_price
                buy = False
            else:
                pass
        return max_profit


a = Solution()
a.maxProfit([2,1,2,0,1])

