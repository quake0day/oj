    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if len(costs) == 0:
        	return 0
        # dp[i][j]: minmum cost painting house 0-i with house i painted with color j
        dp = [[0 for _ in xrange(len(costs[0]))] for _ in xrange(len(costs))]
        for i in xrange(len(costs[0])):
        	dp[0][i] = dp[0][i]

        for i in xrange(1, len(costs)):
        	preMin = sys.maxint
        	preSecondMin = sys.maxint

        	for j in xrange(len(costs[0])):
        		if (dp[i-1][j] <= preMin):
        			preSecondMin = preMin
        			preMin = dp[i-1][j]
        		elif (dp[i-1][j] < preSecondMin):
        			preSecondMin = dp[i-1][j]

        	for j in xrange(len(costs[0])):
        		if dp[i-1][j] == preMin:
        			dp[i][j] = preSecondMin + costs[i][j]
        		else:
        			dp[i][j] = preMin + costs[i][j]
        min_ = sys.maxint
        for j in xrange(len(costs[0])):
        	min_ = min(min_, dp[-1][j])
        return min_
