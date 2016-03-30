class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        maxProfit = 0
        buyPrice = prices[0]
        for i in xrange(1, len(prices)):
            buyPrice = min(prices[i], buyPrice)
            maxProfit = max(maxProfit, prices[i]-buyPrice)
        return maxProfit
            

a = Solution()
print a.maxProfit([2,1,2,0,1])
print a.maxProfit([3,50,4,0,100])