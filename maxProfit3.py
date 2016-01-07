class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        n = len(prices)
        preProfit = [-999]*n
        postProfit = [-999]*n
        
        curMin = prices[0]
        for i in xrange(1,n):
            curMin = min(curMin, prices[i])
            preProfit[i] = max(preProfit[i-1], prices[i]-curMin)
        curMax = prices[n-1]
        for i in xrange(n-2,-1,-1):
            curMax = max(curMax, prices[i])
            postProfit[i] = max(postProfit[i-1], curMax-prices[i])
        maxProfit = 0
        print preProfit, postProfit
        for i in xrange(n):
            maxProfit = max(maxProfit, preProfit[i] + postProfit[i])
        return maxProfit

a = Solution()
print a.maxProfit([2,1,2,0,1])
