class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        r = len(dungeon)
        c = len(dungeon[0])
        dp = [[0] * c for _ in xrange(r)]
        dp[-1][-1] = max(1, 1-dungeon[-1][-1])
        for i in xrange(c-2, -1, -1):
            dp[-1][i] = max(1, dp[-1][i+1]-dungeon[-1][i])
        for i in xrange(r-2, -1, -1):
            dp[i][-1] = max(1, dp[i+1][-1]-dungeon[i][-1])

        for i in xrange(r-2, -1, -1):
            for j in xrange(c-2, -1, -1):
                dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1])-dungeon[i][j])
        return dp[0][0]

