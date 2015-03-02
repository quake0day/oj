class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if len(prices) <= 1:
        	return 0
        low = prices[0]
        maxp = 0

        for i in xrange(1,len(prices)):
        	profit = prices[i] - low
        	if maxp < profit:
        		maxp = profit
        	if low > prices[i]:
        		low = prices[i]
        return maxp

