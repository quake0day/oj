class Solution:
    """
    @param s: A string 
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):
        # write your code here
        dp = [[False for j in xrange(len(p) + 1)] for i in xrange(len(s) + 1)]
        dp[0][0] = True
        for j in xrange(1, len(p) + 1):
        	if p[j-1] == "*":
        		if j >= 2:
        			dp[0][j] = dp[0][j-2]
        for i in xrange(1, len(s) + 1):
        	for j in xrange(1, len(p) + 1):
        		if p[j - 1] == '.':
        			dp[i][j] = dp[i-1][j-1]
        		elif p[j - 1] == "*":										# aa *a case        # .* case
        			dp[i][j] = dp[i][j-1] or dp[i][j-2] or (dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.'))
        		else:
        			dp[i][j] = s[i-1] == p[j-1] and dp[i-1][j-1]
        return dp[-1][-1]