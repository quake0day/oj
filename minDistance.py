class Solution: 
    # @param word1 & word2: Two string.
    # @return: The minimum number of steps.
    def minDistance(self, word1, word2):
        # write your code here
        n = len(word1)
        m = len(word2)

        dp = [[0] * (m+1) for row in xrange(n+1)]
        for i in xrange(m+1):
        	dp[0][i] = i
        for i in xrange(n+1):
        	dp[i][0] = i
        print dp
        for i in xrange(1,n+1):
        	for j in xrange(1,m+1):
        		if word1[i - 1] == word2[j - 1]:
        			dp[i][j] = dp[i-1][j-1]
        		else:
        			dp[i][j] = 1 + min(dp[i-1][j-1], min(dp[i-1][j],dp[i][j-1]))
        return dp[n][m]

a = Solution()
print a.minDistance("aaa","bbbbb")
print a.minDistance("ab","a")