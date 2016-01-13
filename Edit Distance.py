class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        DP = [[0 for _ in xrange(n+1)] for _ in xrange(m+1)]
        for i in xrange(m +1):
            dp[i][0] = i
        for j in xrange(n + 1):
            dp[0][j] = j
        for i in xrange(1, m + 1):
            for j in xrange(1, n+1):
                dp[i][j] = dp[i-1][j-1] if word1[i-1] == word2[j-1] else min(dp[i-1][j-1]+1, dp[i][j-1]+1, dp[i-1][j]+1)
        return dp[m][n]
        
