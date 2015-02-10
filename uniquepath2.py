class Solution:
    """
    @param obstacleGrid: An list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        if (m == 0 or n == 0):
            return 0

        total = [[0] * m for row in xrange(n)]

        for i in xrange(n):
            if obstacleGrid[i][0] != 1:
                total[i][0] = 1
            else:
                break
        for i in xrange(m):
            if obstacleGrid[0][i] != 1:
                total[0][i] = 1
            else:
                break
        for i in xrange(1,n):
            for j in xrange(1,m):
                if obstacleGrid[i][j] != 1:
                    total[i][j] = (total[i][j-1] + total[i-1][j])
                else:
                    total[i][j] = 0
        return abs(total[-1][-1])

        


a = Solution()
print a.uniquePathsWithObstacles([[0,0,0],[0,0,1],[0,0,0],[0,0,0]])
print a.uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,0,0]
])

print a.uniquePathsWithObstacles([[0,0],[0,0],[0,0],[1,0],[0,0]])
