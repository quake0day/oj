class Solution:
    """
    @param grid: a list of lists of integers.
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        n = len(grid)
        m = len(grid[0])

        path_sum = [[0] * m for row in xrange(n)]
        # initialize path_sum
        path_sum[0][0] = grid[0][0]
        for i in xrange(n):
        	for j in xrange(m):
        		if i >= 0 and j >= 0:
        			if i >= 1 and j >= 1:
        				path_sum[i][j] = min(path_sum[i-1][j], path_sum[i][j-1]) + grid[i][j]
        			elif i >= 1 and j < 1:
        				path_sum[i][j] = path_sum[i-1][j] + grid[i][j]
        			else:
        				path_sum[i][j] = path_sum[i][j-1] + grid[i][j]
        return path_sum[-1][-1]

a = Solution()
print a.minPathSum([[1,2,3],[4,5,6],[7,8,9]])