import sys
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0] + [sys.maxint] * amount
        
        for i in xrange(amount):

            for c in coins:
                if c + i > amount:
                    continue
                dp[i+c] = min(dp[i] +1, dp[i+c])
        return dp[-1]

a = Solution()
print a.coinChange([1, 2, 5], 11)